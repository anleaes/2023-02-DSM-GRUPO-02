from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'vehicle'

router = routers.DefaultRouter()
router.register('veiculos', views.VehicleViewSet, basename='veiculos')

urlpatterns = [
    path('', include(router.urls) )
]