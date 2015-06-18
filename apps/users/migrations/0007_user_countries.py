# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20150618_0837'),
        ('users', '0006_auto_20150618_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='countries',
            field=models.ManyToManyField(to='countries.Country'),
        ),
    ]
