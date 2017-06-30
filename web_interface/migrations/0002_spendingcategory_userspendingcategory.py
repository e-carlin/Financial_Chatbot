# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpendingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSpendingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_interface.SpendingCategory')),
            ],
        ),
    ]
