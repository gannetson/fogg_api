from rest_framework import serializers
from apps.users.models import User
from apps.countries.models import Country


class UserSerializer(serializers.ModelSerializer):

    countries = serializers.SlugRelatedField(slug_field='code2', queryset=Country.objects, many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'countries']
