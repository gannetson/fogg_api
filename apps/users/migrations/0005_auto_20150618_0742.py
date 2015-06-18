# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150618_0741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined']},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='created',
            new_name='date_joined',
        ),
    ]
