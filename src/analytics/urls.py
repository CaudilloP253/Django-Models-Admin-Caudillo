from django.urls import path

from analytics import views

urlpatterns = [
    path("sales", views.SalesView, name="sales-analytics"),
]
