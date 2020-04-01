# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-01 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200330_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='product',
        ),
        migrations.AddField(
            model_name='tag',
            name='product',
            field=models.ManyToManyField(related_name='tags', related_query_name='tag', to='products.Product'),
        ),
    ]