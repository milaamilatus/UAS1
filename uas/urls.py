from django.contrib import admin
from django.urls import path
from toko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
]