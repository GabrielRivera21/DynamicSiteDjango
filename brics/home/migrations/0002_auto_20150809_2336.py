# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='description',
            field=models.TextField(help_text=b'Image Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='header',
            field=models.CharField(help_text=b'The title header in home page.', max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='order',
            field=models.IntegerField(help_text=b'Place you want to put this image in the carousel.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='sub_header',
            field=models.TextField(help_text=b'Something you want to say in the image in the home page.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='title',
            field=models.CharField(help_text=b'Image Title', max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
