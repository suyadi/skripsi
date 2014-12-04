from django.db import models
from django.apps.config import MODELS_MODULE_NAME

class Gedung(models.Model):
    nama = models.CharField(max_length=50, verbose_name='Nama Gedung')
    deskripsi = models.TextField(verbose_name='Deskripsi')
    latitude = models.DecimalField(verbose_name='Letak Lintang', decimal_places=16, max_digits=20)
    logitude = models.DecimalField(verbose_name='Letak Bujur', decimal_places=16, max_digits=20)
    def __unicode__(self):
        return self.nama
   
class Ruang(models.Model):
    gedung = models.ForeignKey('Gedung', verbose_name="Gedung")
    ruang = models.CharField(max_length=30, verbose_name="Ruang")
    kapasitas = models.IntegerField(verbose_name="Kapasitas")
    kalender = models.CharField(max_length=100, verbose_name='kalender')
    def __unicode__(self):
        return '%s-%s-%d' % (self.gedung, self.ruang, self.kapasitas)