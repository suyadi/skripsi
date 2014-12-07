# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gedung',
            name='latitude',
            field=models.DecimalField(null=True, verbose_name=b'Letak Lintang', max_digits=20, decimal_places=16, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gedung',
            name='logitude',
            field=models.DecimalField(null=True, verbose_name=b'Letak Bujur', max_digits=20, decimal_places=16, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kampus',
            name='latitude',
            field=models.DecimalField(null=True, verbose_name=b'Letak Lintang', max_digits=20, decimal_places=16, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kampus',
            name='logitude',
            field=models.DecimalField(null=True, verbose_name=b'Letak Bujur', max_digits=20, decimal_places=16, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ruang',
            name='kalender',
            field=models.CharField(max_length=100, null=True, verbose_name=b'kalender', blank=True),
            preserve_default=True,
        ),
    ]
