from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.fields import AutoField, IntegerField
from django.db.models.lookups import IsNull

#Modelo Usuario

""" class UserManager(BaseUserManager):
 def create_user(self, username, password=None):
    '''
    Creates and saves a user with the given username and password.
    '''
    if not username:
        raise ValueError('Users must have an username')
    user = self.model(username=username)
    user.set_password(password)
    user.save(using=self._db)
    return user

 def create_superuser(self, username, password):
    '''
    Creates and saves a superuser with the given username and password.
    '''
    user = self.create_user(
        username=username,

        password=password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 30)
    email = models.EmailField('Email', max_length = 100)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username' """


#Modelo Cliente

class Cliente (models.Model):
    cli_id        = models.AutoField(primary_key = True)
    cli_nombre    = models.CharField('Nombre', max_length = 30)
    cli_apellido  = models.CharField('Apellido', max_length = 30)
    cli_celular   = models.CharField('Celular', max_length = 15)
    cli_direccion = models.CharField('Direccion', max_length = 30)
    cli_recomendaciones = models.TextField('Recomendaciones')

#Modelo Producto

class Producto (models.Model):
    product_id    = models.AutoField(primary_key=True)
    product_name  = models.CharField('Producto', max_length = 100)
    product_price = models.IntegerField('Precio')
    product_tipo  = models.CharField('Tipo', max_length = 100)
    product_descripcion = models.TextField('Descripcion', default="")
    product_valoracion  = models.IntegerField('Valoracion', default=5)


#Modelo Pedido

class Pedido(models.Model):
    pedido_id       = AutoField(primary_key=True),
    pedido_cantidad = IntegerField('Cantidad', default=0)
    pedido_prducto  = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    pedido_cliente  = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)