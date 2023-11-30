from django.shortcuts import render
from .models import Socialnetwork
from rest_framework import viewsets
from .serializer import SocialnetworkSerializer

# Create your views here.

# Após o comentario "# Create your views here." e crie as views "Socialnetwork".

class SocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = Socialnetwork.objects.all()
    serializer_class = SocialnetworkSerializer  