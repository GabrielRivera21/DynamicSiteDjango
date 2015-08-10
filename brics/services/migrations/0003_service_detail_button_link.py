# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20150810_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='detail_button_link',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
