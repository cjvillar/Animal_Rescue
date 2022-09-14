from pydoc import allmethods
from django.shortcuts import render
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework import generics


# Create your views here.
class AnimalListCreate(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalListDelete(generics.RetrieveDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'

class AnimalListUpdate(generics.RetrieveUpdateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'
    