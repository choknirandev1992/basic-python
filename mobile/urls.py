from django.urls import path
from .views import Home,About,Product,EMStracking

urlpatterns = [
    path('',Home, name='mobile-home' ),
    path('about/',About, name='mobile-about' ),
    path('ems/',EMStracking, name='mobile-ems' ),
    path('product/',Product, name='mobile-product' ),
]

