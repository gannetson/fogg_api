from django.db import models

class Country(models.Model):

    name = models.CharField(max_length=200)
    code2 = models.CharField(max_length=2, blank=True, help_text="ISO 3166-1 alpha-2 code")
    code3 = models.CharField(max_length=4, blank=True, help_text="ISO 3166-1 alpha-3 code")
    kml = models.CharField(max_length=500000, blank=True, default="")
    geojson = models.CharField(max_length=500000, blank=True, default="")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'countries'
