# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20150618_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='kml',
            field=models.CharField(default=b'', max_length=50000, blank=True),
        ),
    ]
