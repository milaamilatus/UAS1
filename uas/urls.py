from django.contrib import admin
from django.urls import path
from toko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
]