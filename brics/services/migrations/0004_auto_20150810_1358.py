# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_detail_button_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='detail_button_link',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
