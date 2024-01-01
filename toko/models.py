from django.db import models

class Toko(models.Model):
    product = models.CharField(max_length=255)
    kualitas = models.ImageField(null=True)
    Harga = models.CharField(max_length=255)

def __str__(self):
    return f"{self.Nama}"
