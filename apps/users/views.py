from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from apps.users.models import User
from apps.users.permissions import IsCurrentUser
from apps.users.serializers import UserSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsCurrentUser, )

