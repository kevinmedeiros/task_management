# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('date_created', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('group_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.GroupTask')),
            ],
        ),
    ]