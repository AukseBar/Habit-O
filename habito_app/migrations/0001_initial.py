# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 22:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created', models.DateField(default=datetime.date.today)),
                ('days', models.TextField(default={}, max_length=128)),
                ('achievements', models.TextField(default=b'{"1": 0, "3": 0, "2": 0}', max_length=128)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='habit',
            unique_together=set([('user', 'title')]),
        ),
    ]
