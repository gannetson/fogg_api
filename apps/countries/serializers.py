from rest_framework.serializers import ModelSerializer
from apps.countries.models import Country
from apps.users.models import User


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name', 'code2', 'code3']
