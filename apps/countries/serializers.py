from rest_framework import serializers
from apps.countries.models import Country
from apps.users.models import User


class CountrySerializer(serializers.ModelSerializer):

    id = serializers.CharField(source='code2')

    class Meta:
        model = Country
        fields = ['id', 'name']
