from django.urls import path
from.import views

urlpatterns = [
    path('buah/', views.buah, name='buah.html'),
    path('beli/', views.beli, name='beli.html'),
    path('base/', views.base, name='base.html')
]