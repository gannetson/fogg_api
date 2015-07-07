from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.countries.views import CountryList, CountryDetail, CountryKml, CountryGeoJson
from apps.users.views import UserList, UserDetail
from rest_framework.authtoken import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),

    url(r'^api/users/$', UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>\d+)', UserDetail.as_view(), name='user-detail'),

    url(r'^api/countries/$', CountryList.as_view(), name='country-list'),
    url(r'^api/countries/(?P<code2>\w+)', CountryDetail.as_view(), name='country-detail'),

    url(r'^kml/(?P<code2>\w+)', CountryKml.as_view(), name='country-kml'),
    url(r'^geojson/(?P<code2>\w+)', CountryGeoJson.as_view(), name='country-geo-json')
)
