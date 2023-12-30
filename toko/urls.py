from django.urls import path
from.import views

urlpatterns = [
    path('', views.buah, name='buah.html'),
    path('', views.beli, name='beli.html'),
    path('', views.base, name='base.html')
]