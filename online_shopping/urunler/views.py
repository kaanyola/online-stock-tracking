from django.shortcuts import render
from .models import Urun, Satici
from .serializers import UrunSerializer, SaticiSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

# Create your views here.
class UrunListApiView(ListCreateAPIView):
    queryset = Urun.objects.all()
    serializer_class = UrunSerializer

class UrunDetailApiView(RetrieveAPIView):
    queryset = Urun.objects.all()
    serializer_class = UrunSerializer

class SaticiListApiView(ListCreateAPIView): 
    queryset = Satici.objects.all()
    serializer_class = SaticiSerializer

class SaticiDetailApiView(RetrieveAPIView):
    queryset = Satici.objects.all()
    serializer_class = SaticiSerializer