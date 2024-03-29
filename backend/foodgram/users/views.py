from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import CreateUserSerializer


class CreateUserViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.order_by("pk").all()
    serializer_class = CreateUserSerializer
