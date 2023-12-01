from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = 'Pedidos'
    
class DriverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drivers'
    verbose_name = 'Motoristas'
