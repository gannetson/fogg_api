# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('alpha2_code', models.CharField(help_text=b'ISO 3166-1 alpha-2 code', max_length=2, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
