from django.db import models

# Create your models here.
class Barang(models.Model):
    nama=models.CharField(max_length=255)
    gambar=models.CharField(max_length=255)
    harga=models.PositiveIntegerField()
    detail=models.TextField(default="NULL")
    def __str__(self):
        return self.nama