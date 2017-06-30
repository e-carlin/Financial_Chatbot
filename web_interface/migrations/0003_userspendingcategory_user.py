# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_interface', '0002_spendingcategory_userspendingcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userspendingcategory',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web_interface.User'),
            preserve_default=False,
        ),
    ]
