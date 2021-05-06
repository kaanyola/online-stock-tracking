from django.db import models

# Create your models here.
class Satici(models.Model):
    isim = models.CharField(max_length=50)
    sehir = models.CharField(max_length=50)
    sektor = models.CharField(max_length=50)
    katilma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isim


class Urun(models.Model):
    isim = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    fiyat = models.DecimalField(max_digits=20, decimal_places=2)
    satici = models.ForeignKey(Satici, on_delete=models.CASCADE, default=1, related_name='urunler')
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.isim
    