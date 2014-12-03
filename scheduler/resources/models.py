from django.db import models
from django import forms


class ResourceType(models.Model):
    resource_type = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=100)
    def __unicode__(self):
        return self.description


class CalendarResources(models.Model):
    resource_id = models.CharField(max_length=100)
    resource_common_name = models.CharField(max_length=100)
    resource_description = models.TextField(null=True, blank=True)
    resource_email = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.resource_common_name


class ResourceForm(forms.Form):
    resource_common_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control',}),
        label='Nama sumber daya',
        help_text='Format: [tipe sumber daya]-[kampus dan gedung]-'+
                  '[lantai atau lokasi]-[nama]-[info tambahan]. '+
                  'Contoh: K02J-406-40 (Kampus 2 gedung J '+
                  'ruang 406 kapasitas 40 orang).',
        max_length=100)
    resource_description = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','rows': '4'}), 
        label='Deskripsi')
    resource_type = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class':'form-control',}),
        queryset=ResourceType.objects.all(), 
        label='Tipe sumber daya')
