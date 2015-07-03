from django.contrib import admin
from models import Country


class CountryAdmin(admin.ModelAdmin):

    list_display = ('name', 'code2', 'code3')

admin.site.register(Country, CountryAdmin)
