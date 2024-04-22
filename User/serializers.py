from rest_framework import serializers
from .models import PerfilPawmate


class PerfilPawmateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilPawmate
        fields = '__all__'
        