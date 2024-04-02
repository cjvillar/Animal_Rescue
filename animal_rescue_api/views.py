from pydoc import allmethods

from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Animal
from .serializers import (
    AnimalSerializer,
    UserLoginSerializer,
    UserRegisterSerializer,
    UserSerializer,
)
from .validations import custom_validation, validate_email, validate_password


# Create your views here.
class AnimalListCreate(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalListDelete(generics.RetrieveDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = "pk"


class AnimalListUpdate(generics.RetrieveUpdateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = "pk"


class Animal(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = "pk"


# user views:


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
