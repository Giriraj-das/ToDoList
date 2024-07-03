from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import User
from core.serializers import UserCreateSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserLoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPasswordUpdateView(generics.UpdateAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
