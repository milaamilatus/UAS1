from django.db import models

class toko(models.model):
    Nama_buah = models.CharField(max_lenght=255)
    Jumlah = models.ImageField(null=True)
    Harga = models.CharField(max_lenght=255)

def __str__(self):
    return f"{self.Nama}"
