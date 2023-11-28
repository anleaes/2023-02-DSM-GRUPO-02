from django.db import models
from categories.models import Category


# Create your models here.
class Vehicle(models.Model):
    model = models.CharField('Modelo', max_length=50)
    brand = models.CharField('Marca', max_length=50)
    year = models.IntegerField('Ano do carro') 
    color = models.CharField('Cor', max_length=50)
    is_active = models.BooleanField('Ativo', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
        ordering =['id']

    def __str__(self):
        return self.name