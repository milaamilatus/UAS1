from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'toko/index.html')

def profile(request):
    return render(request, 'toko/profile.html')

def product(request):
    return render(request, 'toko/product.html')

def contact(request):
    return render(request, 'toko/contact.html')