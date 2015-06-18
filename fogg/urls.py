from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.countries.views import CountryList
from apps.users.views import UserList

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/users/', UserList.as_view()),
    url(r'^api/countries/', CountryList.as_view())
)
