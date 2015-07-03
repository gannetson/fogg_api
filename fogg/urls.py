from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.countries.views import CountryList, CountryDetail, CountryKml, CountryGeoJson
from apps.users.views import UserList, UserDetail

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/users/$', UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>\d+)', UserDetail.as_view(), name='user-detail'),

    url(r'^api/countries/$', CountryList.as_view(), name='country-list'),
    url(r'^api/countries/(?P<pk>\d+)', CountryDetail.as_view(), name='country-detail'),

    url(r'^kml/(?P<pk>\d+)', CountryKml.as_view(), name='country-kml'),
    url(r'^geojson/(?P<pk>\d+)', CountryGeoJson.as_view(), name='country-geo-json')
)
