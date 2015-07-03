from django.http.response import HttpResponse
from django.views.generic.detail import DetailView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.countries.models import Country
from apps.countries.serializers import CountrySerializer


class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(RetrieveAPIView):
    model = Country
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class CountryKml(DetailView):
    model = Country
    template_name = 'countries/country_kml.html'

    def get(self, request, *args, **kwargs):
        super(CountryKml, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        country = context['country']
        country.kml = country.kml.replace('kml:', '')
        country.kml = country.kml.replace('ns0:', '')
        country.kml = country.kml.replace('xmlns:kml="http://www.opengis.net/kml/2.2"', '')
        content_type = "application/country-{0}.kml+xml; charset=utf-8".format(country.code)
        return self.render_to_response(context, content_type=content_type)


class CountryGeoJson(DetailView):
    model = Country

    def get(self, request, *args, **kwargs):
        super(CountryGeoJson, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        country = context['country']
        return HttpResponse(country.geojson, content_type='application/json')


