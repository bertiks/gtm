# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=128)),
                ('task_done', models.BooleanField(default=False)),
            ],
        ),
    ]