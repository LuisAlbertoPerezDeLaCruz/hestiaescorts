# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escorts', '0018_escort_es_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('cd_slug', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cd_nombre', models.CharField(max_length=30)),
                ('cd_pais', models.ForeignKey(default='SP', on_delete=django.db.models.deletion.CASCADE, to='escorts.Pais')),
            ],
        ),
        migrations.AlterField(
            model_name='provincia',
            name='pr_pais',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='escorts.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='cd_provincia',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='escorts.Provincia'),
        ),
    ]
