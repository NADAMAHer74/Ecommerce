from django.shortcuts import render
from .models import Category, Products, Blog, About, Slider

def home(request):
    products= Products.objects.all()[:6]
    slider= Slider.objects.all()
    return render(request, 'home.html', {'products':products, 'slider':slider})

def product(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'productDetails.html', {'product':product})

def category(request, category):
    category = category.replace('-', ' ')
    category = Category.objects.get(name=category)
    products = Products.objects.filter(category=category)
    return render(request, 'category.html', {'category':category, 'products':products})

def about(request):
    about = About.objects.all()
    return render(request, 'about.html',{'about':about})

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html',{ 'blog':blog})

def contact(request):
    return render(request, 'contact.html',{ 'contact':contact})

def cart(request):  
    return render(request, 'cart.html',{})

def signup(request):
    return render(request, 'signup.html',{})

def login(request):  
    return render(request, 'login.html',{})

def checkout(request):  
    return render(request, 'checkout.html',{})
