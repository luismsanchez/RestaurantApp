from rest_framework import serializers
from .models import Cliente, Producto, Pedido


# Serializador Cliente

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Cliente
        fields = ['url', 'cli_nombre', 'cli_apellido', 'cli_celular', 'cli_direccion', 'cli_recomendaciones'] 



#Serializador Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Producto
        fields = ['url', 'product_name', 'product_price', 'product_tipo', 'product_descripcion', 'product_valoracion'] 


# Serializador Pedido
class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['url', 'pedido_cantidad', 'pedido_prducto', 'pedido_cliente']



#Serializador Usuario

""" class UserSerializer(serializers.ModelSerializer):
    #account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        #account = Account.objects.get(user=obj.id) 
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            
        } """
       