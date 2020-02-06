from django.contrib.auth.models import  Group
from .models import *
from django_mailbox.models import Message
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

class RestauranteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('id','nombre','tipo','ciudad','dueño','imageUrl')
        extra_kwargs = {
          'dueño': {'write_only': True}
          }
class MenuItemSerializer(serializers.ModelSerializer):
     class Meta:
         model = MenuItem
         fields = '__all__'
class DescPedidoTextSerializer(serializers.ModelSerializer):
    menuItem=serializers.SlugRelatedField(
    slug_field= 'Nombre',
    queryset= MenuItem.objects.all(),
    )
    class Meta:
         model = DescripcionPedido
         fields = ('menuItem','cantidad', 'preciototal', 'pedido')
class DescPedidoSerializer(serializers.ModelSerializer):
    menuItem=serializers.PrimaryKeyRelatedField( queryset= MenuItem.objects.all())
    class Meta:
         model = DescripcionPedido
         fields = ('menuItem','cantidad', 'preciototal', 'pedido')
class PedidoSerializer(serializers.ModelSerializer):
    descpedido= DescPedidoTextSerializer(many=True)
    cliente=serializers.SlugRelatedField(
    slug_field='username',
    queryset= User.objects.all())
    class Meta:
         model = Pedido
         fields = ('id','cliente','descpedido','tiempopedido','total','listo')
    def create(self, validated_data):
        pedidos_data = validated_data.pop('descpedido')
        pedido = Pedido.objects.create(**validated_data)
        for data in pedidos_data:
            DescripcionPedido.objects.create(pedido=pedido, **data)
        return pedido
class CrearPedidoSerializer(serializers.ModelSerializer):
    descpedido= DescPedidoSerializer(many=True,read_only=True)
    cliente= serializers.PrimaryKeyRelatedField(queryset= User.objects.all())
    restaurante= serializers.PrimaryKeyRelatedField(queryset= Restaurante.objects.all())
    class Meta:
         model = Pedido
         fields = ('id','cliente', 'restaurante','descpedido','tiempopedido','total','listo')
class MarcarPedidoSerializer(serializers.ModelSerializer):
    class Meta:
         model = Pedido
         fields = ('id','listo')
class RestauranteAdminSerializer(serializers.ModelSerializer):
    rpedidos = PedidoSerializer(many=True,read_only=True)
    class Meta:
        model = Restaurante
        fields = ('nombre','tipo','ciudad','direccion','rpedidos')
class RestauranteDetailSerializer(serializers.ModelSerializer):
    menuitem= MenuItemSerializer(many=True,read_only=True)
    class Meta:
        model = Restaurante
        fields = ('id','nombre','tipo','ciudad','imageUrl','menuitem')
        extra_kwargs = {
          'dueño': {'write_only': True}
          }

class PedidodetailSerializer(serializers.ModelSerializer):
    descpedido= DescPedidoTextSerializer(many=True)
    restaurante=serializers.SlugRelatedField(
    slug_field='nombre',
    queryset= Restaurante.objects.all(),
    )
    class Meta:
         model = Pedido
         fields = ('id','restaurante','descpedido','tiempopedido','total','listo')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','user_type','password')
        extra_kwargs = {
          'password': {'write_only': True}
          
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
class DueñoUserSerializer(serializers.ModelSerializer):
    dueno = RestauranteListSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = ('id','email','username','user_type','dueno')
class ClienteUserSerializer(serializers.ModelSerializer):
    cpedidos=PedidodetailSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ('id','email','username','user_type','cpedidos')
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'
class ListaIngSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(read_only = True)
    class Meta:
        model = ListaIngredientes
        fields = '__all__'
class PlatoSerializer(serializers.ModelSerializer):
    listaing = ListaIngSerializer(many=True, read_only=True)
    class Meta:
        model = Plato
        fields = ('id','nombre', 'preciohoy', 'listaing', 'descuento')
    
class ListaIngRegisterSerializer(serializers.ModelSerializer):
    ingrediente = serializers.SlugRelatedField(
        queryset = Ingrediente.objects.all(),
        slug_field='nombre'
     )
    class Meta:
        model = ListaIngredientes
        fields = '__all__'