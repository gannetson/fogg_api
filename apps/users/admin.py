from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import User

class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {models.ManyToManyField: {'widget': FilteredSelectMultiple('Countries', is_stacked=False, attrs={'size':'10'})}, }

    list_display = ['email', 'username', 'date_joined', 'country_total']


    readonly_fields = ['last_login', 'date_joined', 'updated', 'country_total']
    fields = readonly_fields + ['username', 'email', 'is_active',
                                'is_staff', 'is_superuser', 'countries']

    def country_total(self, user):
        return len(user.countries.all())

admin.site.register(User, UserAdmin)
