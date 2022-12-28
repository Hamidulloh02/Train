from rest_framework import serializers
from .models import IshHolati, Stansiyalar, Yulak


class IshHolatiSerializers(serializers.ModelSerializer):
    class Meta:
        model = IshHolati
        fields = '__all__'


class StansiyaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stansiyalar
        fields = '__all__'


class YulakSerializers(serializers.ModelSerializer):
    stansiya = StansiyaSerializers()
    go_to = StansiyaSerializers()
    class Meta:
        model = Yulak
        fields = '__all__'
