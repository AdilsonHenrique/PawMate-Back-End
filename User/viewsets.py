from rest_framework import viewsets
from .models import PerfilPawmate
from .serializers import PerfilPawmateSerializer

class PerfilPawmateViewSet(viewsets.ModelViewSet):
    queryset = PerfilPawmate.objects.all()
    serializer_class = PerfilPawmateSerializer