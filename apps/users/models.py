from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models

from django_extensions.db.fields import ModificationDateTimeField, CreationDateTimeField
from apps.countries.models import Country


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField('emailaddress', max_length=254, unique=True, db_index=True)
    username = models.SlugField('username', unique=True)
    date_joined = CreationDateTimeField()
    updated = ModificationDateTimeField()
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)

    countries = models.ManyToManyField(Country)

    objects = UserManager()

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ['-date_joined']

