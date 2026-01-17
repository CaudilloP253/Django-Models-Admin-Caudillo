from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from products.views import (
    ProductDetailView,
    ProductListView, 
    DigitalProductListView, 
    ProductIDRedirectView, 
    ProtectedProductDetailView, 
    ProductRedirectView,
    ProtectedProductCreateView,
    ProtectedProductUpdateView, 
    ProtectedProductDeleteView, 
)

urlpatterns= [
    path("admin/", admin.site.urls),
    # path("about-us/", RedirectView.as_view(url="/products/about/")),
    # path("about/", TemplateView.as_view(template_name="about.html")),
    
    path("products/<slug:slug>/", ProductDetailView.as_view()),
    path("team/", TemplateView.as_view(template_name="team.html")),
    path("products/", ProductListView.as_view()),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product-list"),
    path("digital-products/", DigitalProductListView.as_view()),
    path("p<int:pk>/", ProductIDRedirectView.as_view()),
    path("p/<slug:slug>/", ProductRedirectView.as_view()),
   # path("my-products/<slug:slug>/", ProtectedProductDetailView.as_view()),
    path("my-products/create/", ProtectedProductCreateView.as_view()),

    path ("my-products/<slug:slug>/", ProtectedProductUpdateView.as_view()),
    path ("my-products/<slug:slug>/delete/", ProtectedProductDeleteView.as_view()),
    path("my-products/", ProtectedListView.as_view()),
]
