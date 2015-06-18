from rest_framework.serializers import ModelSerializer
from apps.countries.serializers import CountrySerializer
from apps.users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'countries']
