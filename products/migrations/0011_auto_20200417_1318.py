# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-17 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200407_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('C', 'Cleanser'), ('EX', 'Exfoliator'), ('SE', 'Serum'), ('M', 'Moisturiser'), ('SU', 'Sunscreen'), ('T', 'Toner'), ('FM', 'Face Mask'), ('E', 'Eye Cream')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.CharField(choices=[('EC', 'Eczema'), ('PS', 'Psoriasis'), ('AC', 'Acne'), ('RO', 'Rosacea'), ('D', 'Dry Skin'), ('O', 'Oily Skin'), ('S', 'Sensitive'), ('TI', 'Tired Skin'), ('AG', 'Aging Skin'), ('CE', 'Cellulite'), ('SC', 'Scarring'), ('SU', 'Sun')], max_length=2),
        ),
    ]