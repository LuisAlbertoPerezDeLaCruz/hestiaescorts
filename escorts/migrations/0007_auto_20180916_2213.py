# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-16 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escorts', '0006_auto_20180916_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escort',
            name='es_foto_1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
