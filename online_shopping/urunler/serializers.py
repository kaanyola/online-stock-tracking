from rest_framework import serializers
from .models import Urun, Satici

class SaticiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satici
        fields = '__all__' 

class UrunSerializer(serializers.ModelSerializer):
    satici = SaticiSerializer()
    class Meta:
        model = Urun
        fields = '__all__' 
