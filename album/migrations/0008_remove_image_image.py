# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0007_image_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]
