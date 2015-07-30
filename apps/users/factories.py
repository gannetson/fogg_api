import factory
from apps.countries.models import Country
from apps.users.models import User


class UserFactory(factory.DjangoModelFactory):

    username = factory.Sequence(lambda n: u'user_{0}'.format(n))
    email = factory.Sequence(lambda o: u'user_{0}@fogg.ibizit.nl'.format(o))
    password = factory.PostGenerationMethodCall('set_password', 'testing')
    is_active = True

    class Meta:
        model = User

class UserCountryFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    country = Country.objects.order_by('?')[0]

    class Meta:
        model = UserCountry
