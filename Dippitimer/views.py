
from django.shortcuts import render
from Dippitimer.models import *
from Dippitimer.serializers import *
from Dippitimer.permissions import IsOwnerOrReadOnly,IsClientOrReadOnly,OnlyUser
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from datetime import date
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django_mailbox.models import Message

# Create your views here.
class RestauranteList(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteListSerializer
class TagList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
class RestauranteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteDetailSerializer
class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
class RestauranteAdminList(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteAdminSerializer
class RestauranteAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteAdminSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
class PedidosAdminList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
class PedidosList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = CrearPedidoSerializer
class PedidosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = CrearPedidoSerializer
class MarcarPedidos(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = MarcarPedidoSerializer
class DescPedidosAdminList(generics.ListCreateAPIView):
    queryset = DescripcionPedido.objects.all()
    serializer_class = DescPedidoSerializer
class DescPedidosList(generics.ListCreateAPIView):
    queryset = DescripcionPedido.objects.all()
    serializer_class = DescPedidoSerializer
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class MessageList(generics.ListCreateAPIView):
        queryset = Message.objects.all()
        serializer_class = MessageSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class DueñoUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DueñoUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,OnlyUser]
class ClienteUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ClienteUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,OnlyUser]
class IngredienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class IngredienteList(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ListaIngredienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListaIngredientes.objects.all()
    serializer_class = ListaIngSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ListaIngredienteList(generics.ListCreateAPIView):
    queryset = ListaIngredientes.objects.all()
    serializer_class = ListaIngSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ListaIngredienteRegisterList(generics.ListCreateAPIView):
    queryset = ListaIngredientes.objects.all()
    serializer_class = ListaIngRegisterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class PlatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class PlatoList(generics.ListCreateAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class FiltIngredienteList(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        """
        Filtrar por categorias
        """
        cats = ['Hortalizas/Verduras','Frutas','Tuberculos','Platanos','Granos y Procesados', 'Lacteos', 'Carnes y Pescados', 'Huevos']
        return Ingrediente.objects.filter(categoria=cats[self.kwargs['cat']])