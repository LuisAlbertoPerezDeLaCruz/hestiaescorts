# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-30 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escorts', '0015_auto_20180930_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='hestiainfo',
            name='hi_pais',
            field=models.ForeignKey(blank=True, default='SP', null=True, on_delete=django.db.models.deletion.CASCADE, to='escorts.Pais'),
        ),
    ]
