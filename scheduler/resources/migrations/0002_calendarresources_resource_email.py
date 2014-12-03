# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarresources',
            name='resource_email',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
