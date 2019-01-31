# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-31 07:17
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_productfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\OSAMA\\Desktop\\e-commerce\\static_cdn\\protected_media'), upload_to=products.models.upload_product_file_loc),
        ),
    ]