from django import forms
from .models import *

CATEGORIA_OPCIONES = [('peliculas', 'Peliculas'), ('musica', 'Musica'), 
                      ('series', 'Series'), ('videojuego', 'Videojuego'), 
                      ('documentales', 'Documentales'), ('juegos_de_mesa', 'Juegos de mesa'), 
                      ('cocina', 'Cocina'), ('deportes', 'Deportes'), ('tv', 'TV'), ('arte', 'Arte'), 
                      ('fotografias', 'Fotografias'), ('libros', 'Libros'), ('carreras', 'Carreras'), 
                      ('pelea', 'Pelea'), ('otro', 'Otro'),]
CATEGORIA_OPCIONES = sorted(CATEGORIA_OPCIONES, key=lambda x: x[1])


class ComunidadesForm(forms.Form):
    nombre = forms.CharField(max_length=255)
    fecha_salida = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    categoria = forms.CharField(max_length=255, widget=forms.Select(choices=CATEGORIA_OPCIONES))
    empresa = forms.CharField(max_length=255)
    descripcion = forms.CharField(max_length=255)

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ('__all__')

class BuscarNombre(forms.Form):
    nombre = forms.CharField(label='Nombre de la comunidad', max_length=255)

class BuscarCategoria(forms.Form):
    categoria = forms.CharField(label='Nombre del género', max_length=255, widget=forms.Select(choices=CATEGORIA_OPCIONES))

class BuscarEmpresa(forms.Form):
    empresa = forms.CharField(label='Nombre de la empresa', max_length=255)

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']