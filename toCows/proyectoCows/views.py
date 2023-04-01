#from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Cows
from .models import BornCows
from .models import photo

from .serializers import PhotoSerializer, CowsSerializer, BornSerializer

# Create your views here.

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = photo.objects.all()
    serializer_class = PhotoSerializer

class CowsViewSet(viewsets.ModelViewSet):
    queryset = Cows.objects.all()
    serializer_class = CowsSerializer

class BornCowsViewSet(viewsets.ModelViewSet):
    queryset = BornCows.objects.all()
    serializer_class = BornSerializer