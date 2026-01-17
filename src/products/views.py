# from django.views.generic import View, ListView
#from django.views.generic import TemplateView, View, RedirectView
from django.views.generic import (
    View, 
    ListView, 
    DetailView, 
    RedirectView,
    CreateView,
    UpdateView,
    DeleteView,
    ProtectedListView,
)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product, DigitalProduct
from .mixins import TemplateTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductModelForm

class ProductIDRedirectView(RedirectView):
    def get_redirect_url(self, request, *args, **kwargs):
        url_params = self.kwargs
        pk= url_params.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        slug= obj.slug 
        return f"/products/products/(slug)"
    
class ProductRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        slug= url_params.get("slug")
        return f"/products/products/(slug)"

class ProductListView(TemplateTitleMixin, ListView):
    model = Product
    title = "Productos Físicos"

class ProductDetailView(DetailView):
    model = Product

class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template_name ="products/product_list.html"
    title = "Productos Digitales"
    
class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product

class ProtectedProductDetailView(DetailView, LoginRequiredMixin):
    model = Product

class ProtectedProductCreateView(LoginRequiredMixin, CreateView):
    form_class= ProductModelForm
    template_name= "forms.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
        
class ProtectedProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class= ProductModelForm
    template_name= "products/product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
        
    def get_success_url(self):
        return self.object.get_edit_url()

class ProtectedProductDeleteView(LoginRequiredMixin, DeleteView):
    form_class= "forms-delete.html"
    template_name= "products/product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
        
    def get_success_url(self):
        return "/products/products"
        
class ProtectedListView(LoginRequiredMixin,TemplateTitleMixin, ListView):
    model = Product
    title = "Productos Físicos"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    
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
