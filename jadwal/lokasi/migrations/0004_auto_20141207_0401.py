# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0003_auto_20141207_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ruang',
            options={'verbose_name_plural': 'Ruang'},
        ),
        migrations.RemoveField(
            model_name='ruang',
            name='ruang',
        ),
        migrations.AddField(
            model_name='ruang',
            name='nama',
            field=models.CharField(default=datetime.datetime(2014, 12, 7, 4, 1, 6, 383730, tzinfo=utc), max_length=30, verbose_name=b'Nama Ruang'),
            preserve_default=False,
        ),
    ]
