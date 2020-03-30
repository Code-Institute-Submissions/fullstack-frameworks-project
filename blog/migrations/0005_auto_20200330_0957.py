# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-30 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200328_1802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-published_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(default='Melissa Biggs', max_length=200),
        ),
    ]
