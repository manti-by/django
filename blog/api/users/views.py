from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.users.serializers import UserModelSerializer, UserSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    API endpoint that allows get user.
    """

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    """
    API endpoint that allows to create users.
    """

    serializer_class = UserSerializer
    permission_classes = []

    def perform_create(self, serializer):
        user = User(
            username=serializer.validated_data["email"],
            email=serializer.validated_data["email"],
        )
        user.set_password(serializer.validated_data["password"])
        user.save()


class UserLoginView(GenericAPIView):
    """
    API endpoint that allows to login users.
    """

    serializer_class = UserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.POST)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request=request,
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user is not None:
            login(request, user)
            return Response()

        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(GenericAPIView):
    """
    API endpoint that allows to login users.
    """

    permission_classes = []

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return Response()
