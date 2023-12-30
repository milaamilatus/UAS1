from django.contrib import admin
from .models import toko

# Register your models here.

class MemberToko():
    list_display = ("Nama_buah","Jumlah", "Harga")

admin.site.register(toko)
