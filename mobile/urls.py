from django.urls import path
from .views import Home,About,Product

urlpatterns = [
    path('',Home, name='mobile-home' ),
    path('about/',About, name='mobile-about' ),
    path('product/',Product, name='mobile-product' ),
]
