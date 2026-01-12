# from django.views.generic import View, ListView
#from django.views.generic import TemplateView, View, RedirectView
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product, DigitalProduct

class ProductListView(ListView):
    model = Product
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context["title"]= "Mi fabuloso ecommerce"
        return context

class ProductDetailView(DetailView):
    model = Product

class DigitalProductListView(ListView):
    model = DigitalProduct
    template_name ="products/product_list.html"
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context["title"]= "Mi fabuloso ecommerce"
        return context







# from django.decorators.http import require_http_methods

# from .models import Product

# def products_list_view(request):
#     if request.method == "POST":
#         print(request.POST)
#     print(request.method == "POST")
#     return render(request, "template", {})

# class ProductHomeView(View):
#     def get(self, *args, **kargs):
#         return render(request, "template", {})
    
#     def post(self, *args, **kargs):
#         print(request.POST)
#         return render (render, "template", {})

# class ProductListView(ListView):
#     queryset = Product.objects.all()

# products_list_view = ProductListView.as_view()

# class BlogPostListView(ListView):
#     queryset = Push.objects.all()

# class UserPostListView(ListView):
#     queryset= User.objects.all()

# def abaout_us_view(request):
#     return render(request, "about.html", {})

# class AboutUsView(View):
#     def get(self, request):
#         return render(request, "about.html", {})


# def about_us_redirect_view(request):
#     return HttpReponseRedirect("/about/")
# class AboutUsRedirectView(RedirectView):
#     url= "/products/about/"
