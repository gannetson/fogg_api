# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_country_code3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='code',
            new_name='code2',
        ),
    ]
