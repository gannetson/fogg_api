from rest_framework.generics import ListAPIView
from apps.countries.models import Country
from apps.countries.serializers import CountrySerializer


class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
