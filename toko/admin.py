from django.contrib import admin
from .models import Toko

# Register your models here.

class MemberToko():
    list_display = ("product","kualitas", "Harga")

admin.site.register(Toko)
