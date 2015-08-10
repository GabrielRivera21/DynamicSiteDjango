# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photos')),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True)),
                ('header', models.CharField(max_length=45, blank=True)),
                ('sub_header', models.CharField(max_length=60, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photos', blank=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
