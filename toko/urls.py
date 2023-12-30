from django.urls import path
from.import views

urlpatterns = [
    path('home/', views.home, name='home.html'),
    path('harga/', views.harga, name='harga.html'),
    path('about/', views.about, name='about.html'),
    path('index/', views.index, name='index.html')
]