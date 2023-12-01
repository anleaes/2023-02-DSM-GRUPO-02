from django.shortcuts import render
from .models import Order, Driver
from rest_framework import viewsets
from .serializer import OrderSerializer, DriverSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
    
class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer  
