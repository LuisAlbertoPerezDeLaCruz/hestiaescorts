# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-07 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escorts', '0021_auto_20181002_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciosescort',
            name='se_escort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escorts.Escort'),
        ),
    ]
