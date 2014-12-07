# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gedung',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=50, verbose_name=b'Nama Gedung')),
                ('deskripsi', models.TextField(verbose_name=b'Deskripsi', blank=True)),
                ('latitude', models.DecimalField(verbose_name=b'Letak Lintang', max_digits=20, decimal_places=16, blank=True)),
                ('logitude', models.DecimalField(verbose_name=b'Letak Bujur', max_digits=20, decimal_places=16, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Gedung',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kampus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=50, verbose_name=b'Nama Kampus')),
                ('alamat', models.CharField(max_length=255, verbose_name=b'Alamat')),
                ('latitude', models.DecimalField(verbose_name=b'Letak Lintang', max_digits=20, decimal_places=16, blank=True)),
                ('logitude', models.DecimalField(verbose_name=b'Letak Bujur', max_digits=20, decimal_places=16, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Kampus',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ruang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruang', models.CharField(max_length=30, verbose_name=b'Ruang')),
                ('kapasitas', models.IntegerField(verbose_name=b'Kapasitas')),
                ('kalender', models.CharField(max_length=100, verbose_name=b'kalender', blank=True)),
                ('gedung', models.ForeignKey(verbose_name=b'Gedung', to='lokasi.Gedung')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gedung',
            name='lokasi',
            field=models.ForeignKey(verbose_name=b'Lokasi Kampus', to='lokasi.Kampus'),
            preserve_default=True,
        ),
    ]
