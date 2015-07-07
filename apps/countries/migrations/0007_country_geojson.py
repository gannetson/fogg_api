# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0006_auto_20150702_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='geojson',
            field=models.CharField(default=b'', max_length=500000, blank=True),
        ),
    ]
