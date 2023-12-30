from django.db import models

class toko(models.Model):
    Nama_buah = models.CharField(max_length=255)
    Jumlah = models.ImageField(null=True)
    Harga = models.CharField(max_length=255)

def __str__(self):
    return f"{self.Nama}"
