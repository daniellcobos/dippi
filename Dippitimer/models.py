from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  email = models.EmailField(max_length=254, unique=True)
  USER_TYPE_CHOICES = (
      (1, 'Administrador de Restaurante'),
      (2, 'Usuario'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
  def __str__(self):
        return self.email
class Restaurante(models.Model):
    nombre = models.CharField(blank=True, max_length=255)
    direccion = models.CharField(blank=True, max_length=255)
    tipo = models.CharField(blank=True, max_length=55)
    ciudad = models.CharField(blank=True, max_length=55)
    dueño = models.ForeignKey(User, related_name=("dueno"), on_delete=models.CASCADE)
    imageUrl = models.CharField(blank=True, max_length=255)
    def __str__(self):
        return self.nombre
class MenuItem(models.Model):
    Nombre = models.CharField(max_length=55)
    imageUrl= models.CharField(blank=True, max_length=255)
    Precio = models.IntegerField()
    Descrpicion = models.CharField(blank=True, max_length=255)
    restaurante = models.ForeignKey(Restaurante, related_name='menuitem', on_delete=models.CASCADE)    
    def __str__(self):
        return str(self.Nombre)
class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(User, related_name='cpedidos', on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, related_name='rpedidos', on_delete=models.CASCADE)
    tiempopedido = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    listo = models.BooleanField(default=False)
    entregado = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
class DescripcionPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='descpedido', on_delete=models.CASCADE)
    menuItem = models.ForeignKey(MenuItem, related_name='item', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    preciototal = models.IntegerField()
    def __str__(self):
        return str(self.id)
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=56)
    preciohoy = models.IntegerField( default = 0)
    precioayer = models.IntegerField( default = 0)
    descuento = models.BooleanField ( default = False)
    unidad = models.CharField(max_length=55)
    categoria = models.CharField(max_length=55)
   
    def __str__(self):
        return str(self.nombre)
class Plato(models.Model):
    id = models.IntegerField(primary_key=True)
    creador = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=55)
    preciohoy = models.DecimalField(max_digits = 14, decimal_places=3 , default = 0)
    precioayer = models.DecimalField(max_digits = 14, decimal_places=3, default = 0)
    descuento = models.BooleanField ( default = False)
    def __str__(self):
        return str(self.nombre)
class ListaIngredientes(models.Model):
    ingrediente = models.ForeignKey(Ingrediente,related_name="platos", on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, related_name="listaing", on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits = 7,decimal_places=3)
    
    def __str__(self):
        return str(self.id)
