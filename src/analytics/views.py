from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
from django.shortcuts import render
from typing import Any
from django.db.models import Sum
from django.utils import timezone
from django.http.request import HttpRequest as HttpRequest
from django.db.models.functions import TruncDay

from datetime import timedelta

from order.models import Order

class SalesView(LoginRequiredMixin, TemplateView):
    template_name="analytics/sales.html"

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(SalesView,self).dispatch( *args, **kwargs)
    
    def get_context_data(self,*args, **kwargs):
        context= super(SalesView, self).get_context_data(*args, **kwargs)
        qs= Order.objects.all()
        context["orders"]= qs
        context["recent_orders"]= qs.recent().not_refunded()[:5]
        context["shipped_orders"]= qs.recent().not_refunded().by_status(status="shipped")[:5]
        context["paid_orders"]= qs.recent().not_refunded().by_status(status="paid")[:5]
        print(context)
        return context

class SalesAjaxView(View):
    def get(self, request, *args, **kwargs):
        sales_type = request.GET.get("type", "week")
        today = timezone.now()

        if sales_type == "week":
            start_date = today - timedelta(days=7)
        elif sales_type == "month":
            start_date = today - timedelta(days=30)
        else:
            start_date = today - timedelta(days=7)

        qs = (
            Order.objects
            .filter(updated__gte=start_date, status="paid")
            .annotate(day=TruncDay("updated"))
            .values("day")
            .annotate(total=Sum("total"))
            .order_by("day")
        )

        labels = []
        data = []

        for item in qs:
            labels.append(item["day"].strftime("%d %b"))
            data.append(item["total"])

        return JsonResponse({
            "labels": labels,
            "data": data
        })

