
from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path ('', views.home, name='home'),
    path ('product/<int:pk>', views.product, name='product'),
    path ('category/<str:category>', views.category, name='category'),
    path ('about', views.about, name='about'),
    path ('blog', views.blog, name='blog'),
    path ('contact', views.contact, name='contact'),
    path ('cart', views.cart, name='cart'),
    path ('signup', views.signup, name='signup'),
    path ('login', views.login, name='login'),
    path ('checkout', views.checkout, name='checkout'),





]
