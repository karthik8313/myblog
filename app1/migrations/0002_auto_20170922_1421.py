# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='hero',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]