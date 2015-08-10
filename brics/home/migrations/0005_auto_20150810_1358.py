# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_feature_detail_button_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='detail_button_link',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
