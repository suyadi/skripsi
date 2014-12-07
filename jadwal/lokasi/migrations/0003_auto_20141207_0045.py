# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0002_auto_20141206_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='kampus',
            name='deskripsi',
            field=models.TextField(default=datetime.datetime(2014, 12, 7, 0, 45, 4, 491184, tzinfo=utc), verbose_name=b'Deskripsi', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ruang',
            name='kalender',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Kalender ID', blank=True),
            preserve_default=True,
        ),
    ]
