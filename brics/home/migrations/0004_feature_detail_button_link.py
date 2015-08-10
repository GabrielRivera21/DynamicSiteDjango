# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='detail_button_link',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
