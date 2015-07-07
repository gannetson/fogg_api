# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_country_kml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='kml',
            field=models.CharField(default=b'', max_length=500000, blank=True),
        ),
    ]
