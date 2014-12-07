from django.db import models

class Kampus(models.Model):
    nama = models.CharField(max_length=50, verbose_name='Nama Kampus')
    deskripsi = models.TextField(verbose_name='Deskripsi', blank=True)
    alamat = models.CharField(max_length=255, verbose_name='Alamat')
    latitude = models.DecimalField(verbose_name='Letak Lintang', decimal_places=16, max_digits=20, null=True, blank=True)
    logitude = models.DecimalField(verbose_name='Letak Bujur', decimal_places=16, max_digits=20, null=True, blank=True)
    def __unicode__(self):
        return '%s: %s' % (self.nama, self.deskripsi)
    class Meta():
        verbose_name_plural="Kampus"
    

class Gedung(models.Model):
    lokasi = models.ForeignKey('Kampus', verbose_name='Lokasi Kampus')
    nama = models.CharField(max_length=50, verbose_name='Nama Gedung')
    deskripsi = models.TextField(verbose_name='Deskripsi', blank=True)
    latitude = models.DecimalField(verbose_name='Letak Lintang', decimal_places=16, max_digits=20, null=True, blank=True)
    logitude = models.DecimalField(verbose_name='Letak Bujur', decimal_places=16, max_digits=20, null=True, blank=True)
    def __unicode__(self):
        return '%s: %s' % (self.nama, self.deskripsi)
    class Meta():
        verbose_name_plural="Gedung"
   
class Ruang(models.Model):
    gedung = models.ForeignKey('Gedung', verbose_name="Gedung")
    nama = models.CharField(max_length=30, verbose_name="Nama Ruang")
    kapasitas = models.IntegerField(verbose_name="Kapasitas")
    kalender = models.CharField(max_length=100, verbose_name='Kalender ID', null=True, blank=True)
    def __unicode__(self):
        return '%s-%d' % (self.nama, self.kapasitas)
    class Meta():
        verbose_name_plural="Ruang"
    