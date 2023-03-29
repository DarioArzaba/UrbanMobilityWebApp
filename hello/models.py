from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Producto(models.Model):
    category = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20) 
    price = models.CharField(max_length = 20)
    minimal = models.CharField(max_length = 20)

class Provedores(models.Model):
    categoryPedido = models.CharField(max_length = 20)
    titlePedido = models.CharField(max_length = 20) 
    pricePedido = models.CharField(max_length = 20)
    minimalPedido = models.CharField(max_length = 20)