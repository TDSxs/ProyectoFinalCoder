from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORIA_OPCIONES = [('peliculas', 'Peliculas'), ('musica', 'Musica'), 
                      ('series', 'Series'), ('videojuego', 'Videojuego'), 
                      ('documentales', 'Documentales'), ('juegos_de_mesa', 'Juegos de mesa'), 
                      ('cocina', 'Cocina'), ('deportes', 'Deportes'), ('tv', 'TV'), ('arte', 'Arte'), 
                      ('fotografias', 'Fotografias'), ('libros', 'Libros'), ('carreras', 'Carreras'), 
                      ('pelea', 'Pelea'), ('otro', 'Otro'),]

CATEGORIA_OPCIONES = sorted(CATEGORIA_OPCIONES, key=lambda x: x[1])

VALORACIONES_OPCIONES = [(i, str(i)) for i in range(1, 11)]

class Comunidad(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_salida = models.DateField()
    categoria = models.CharField(max_length=255, choices=CATEGORIA_OPCIONES)
    empresa = models.CharField(max_length=255)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.nombre} - {self.categoria} - {self.empresa}"

class Resena(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.autor} - {self.comunidad.nombre}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} / {self.imagen}"
    
class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.creador} - {self.titulo}"

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='comentarios')
    def __str__(self):
        return f"{self.creador} - {self.tema}"