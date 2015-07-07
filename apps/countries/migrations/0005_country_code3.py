# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_auto_20150619_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='code3',
            field=models.CharField(help_text=b'ISO 3166-1 alpha-3 code', max_length=4, blank=True),
        ),
    ]
