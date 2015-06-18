# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20150618_0837'),
        ('users', '0007_user_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True)),
                ('country', models.ForeignKey(to='countries.Country')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='countries',
        ),
        migrations.AddField(
            model_name='usercountry',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
