from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def buah(request):
    template = loader.get_template('buah.html')
    return HttpResponse(template.render())

def beli(request):
    template = loader.get_template('beli.html')
    return HttpResponse(template.render())

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

