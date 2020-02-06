from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
app_name= 'Dippi'
urlpatterns = [
    path('restaurantes', views.RestauranteList.as_view()),
    path('restaurantes/<int:pk>', views.RestauranteDetail.as_view()),
    path('misrestaurantes', views.RestauranteAdminList.as_view()),
    path('misrestaurantes/<int:pk>', views.RestauranteAdminDetail.as_view()),
    path('pedidos', views.PedidosAdminList.as_view()),
    path('pedidos/<int:pk>', views.PedidosDetail.as_view()),
    path('marcarpedidos/<int:pk>', views.MarcarPedidos.as_view()),
    path('crearpedidos', views.PedidosList.as_view()),
    path('descpedidos', views.DescPedidosAdminList.as_view()),
    path('rdescpedidos', views.DescPedidosList.as_view()),
    path('userlist', views.UserList.as_view()),
    path('clientdetail/<int:pk>', views.ClienteUserDetail.as_view()),
    path('duenodetail/<int:pk>', views.DueñoUserDetail.as_view()),
    path('menuitem', views.MenuItemList.as_view()),
    path('ingrediente', views.IngredienteList.as_view()),
    path('ingrediente/<int:pk>', views.IngredienteDetail.as_view()),
    path('listaingrediente', views.ListaIngredienteList.as_view()),
    path('listaingregister', views.ListaIngredienteRegisterList.as_view()),
    path('listaingrediente/<int:pk>', views.ListaIngredienteDetail.as_view()),
    path('plato', views.PlatoList.as_view()),
    path('plato/<int:pk>', views.PlatoDetail.as_view()),
    path('message', views.MessageList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),

    ]