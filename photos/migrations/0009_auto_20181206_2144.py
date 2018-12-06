# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20181206_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('Category', models.ManyToManyField(to='photos.Category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='location',
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['location']},
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=60),
        ),
        migrations.DeleteModel(
            name='categorys',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]