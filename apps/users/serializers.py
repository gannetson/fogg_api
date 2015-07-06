from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    countries = serializers.SlugRelatedField(slug_field='code2', queryset='countries', many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'countries']
