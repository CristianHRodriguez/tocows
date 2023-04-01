from rest_framework import serializers
from .models import photo
from .models import Cows
from .models import BornCows

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = '__all__'

class CowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cows
        fields = '__all__'

class BornSerializer(serializers.ModelSerializer):
    class Meta:
        model = BornCows
        fields = '__all__'