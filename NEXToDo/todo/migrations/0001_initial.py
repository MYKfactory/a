# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-23 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='Todo')),
                ('pub_date', models.DateTimeField(verbose_name='締め切り')),
            ],
        ),
    ]
