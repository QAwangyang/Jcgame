# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-19 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users_car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('isvisit', models.IntegerField()),
                ('car_counts', models.IntegerField()),
                ('multiple', models.IntegerField()),
                ('visittime', models.CharField(max_length=50)),
            ],
        ),
    ]
