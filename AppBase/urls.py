from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('ag-comunidad', agregar_comunidad, name="AgregarComunidad"),
    path('l-comunidades', lista_comunidad, name="ListaComunidades"),
    path('el-comunidades/<int:id>', eliminar_comunidades, name="EliminarComunidad"),
    path('ed-comunidades/<int:id>', editar_comunidades, name="EditarComunidad"),
    path('ag-resena', agregar_resena, name='AgregarResena'),
    path('l-resenas', lista_resenas, name='ListaResenas'),
    path('el-resenas/<int:id>', eliminar_resena, name="EliminarResena"),
    path('ed-resenas/<int:id>', editar_resena, name="EditarResena"),
    path('busq-comunidad', busqueda_comunidades, name="BusquedaComunidades"),
    path('buscar-nombre', buscar_nombre, name="BuscarNombre"),
    path('buscar-categoria', buscar_categoria, name="BuscarCategoria"),
    path('buscar-empresa', buscar_empresa, name="BuscarEmpresa"),
    path('about-me', AboutMe, name="AboutMe"),
    path('foro', lista_temas, name='Foro'),
    path('crear-tema', crear_tema, name='CrearTema'),
    path('ed-tema/<int:pk>', editar_tema, name='EditarTema'),
    path('el-tema/<int:pk>', eliminar_tema, name='EliminarTema'),
    path('foro/<int:pk>/', detalle_tema, name='DetalleTema'),
    path('<int:pk>/crear-coment', crear_comentario, name='CrearComentario'),
]