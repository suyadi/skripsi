from django.contrib import admin
from lokasi.models import Gedung, Ruang

class RuangTabular(admin.TabularInline):
    model = Ruang
    extra = 1

class GedungAdmin(admin.ModelAdmin):
    inlines = (RuangTabular,) 

admin.site.register(Gedung)
