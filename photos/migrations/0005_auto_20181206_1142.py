# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20181206_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='categorys',
            field=models.ManyToManyField(default=True, to='photos.Categorys'),
        ),
    ]
