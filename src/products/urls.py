from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from products.views import ProductDetailView, ProductListView, DigitalProductListView

urlpatterns= [
    path("admin/", admin.site.urls),
    # path("about-us/", RedirectView.as_view(url="/products/about/")),
    # path("about/", TemplateView.as_view(template_name="about.html")),
    path("team/", TemplateView.as_view(template_name="team.html")),
    path("products/", ProductListView.as_view()),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product-list"),
    path("digital-products/", DigitalProductListView.as_view()),
]