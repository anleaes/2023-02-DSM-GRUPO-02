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
    order = models.ManyToManyField(Vehicle, through='OrderItem', blank=True)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.total_price) 


class OrderItem(models.Model):
    status = models.CharField('Status', max_length=20)
    total_price = models.DecimalField('Preco total', decimal_places=2, max_digits=12, null=True, blank=True, default=0.0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Carro de pedido'
        verbose_name_plural = 'Carros'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity) 
