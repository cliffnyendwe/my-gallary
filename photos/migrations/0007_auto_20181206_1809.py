# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20181206_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ManyToManyField(default=True, to='photos.Categorys'),
        ),
    ]
