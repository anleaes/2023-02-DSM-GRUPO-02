from django.db import models
from vehicle.models import Vehicle
from clients.models import Client


# Create your models here.

class Order(models.Model):
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ManyToManyField(Vehicle, through='Driver', blank=True)
    payment_method = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.total_price) 


class Driver(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver_first_name = models.CharField(max_length= 255)
    driver_last_name = models.CharField(max_length= 255)
    driver_adress = models.CharField(max_length= 255)
    driver_cellphone = models.IntegerField(max_length= 20)
    driver_email = models.EmailField()
    license = models.IntegerField(max_length=100)
    
    

    class Meta:
        verbose_name = 'Carro de pedido'
        verbose_name_plural = 'Carros'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.driver_first_name) (self.driver_last_name)
