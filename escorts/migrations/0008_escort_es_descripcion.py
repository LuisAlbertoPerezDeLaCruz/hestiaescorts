# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-16 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escorts', '0007_auto_20180916_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='escort',
            name='es_descripcion',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
