from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=2, blank=True, help_text="ISO 3166-1 alpha-2 code")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'countries'
