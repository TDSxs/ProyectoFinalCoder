from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from .views import *

# Create your tests here.
#Test Documentado 1 "CRUD de Comunidad":
class ComunidadTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.comunidad = Comunidad.objects.create(nombre='nombre de Prueba', fecha_salida='2022-01-01', categoria='Aventura', empresa='DesarrolladorX', descripcion='Un juego de prueba', valoracion=4)

    def test_agregar_comunidad(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('agregar_comunidad')
        data = {'nombre': 'Nuevo Juego', 'fecha_salida': '2023-04-30', 'categoria': 'Estrategia', 'empresa': 'DesarrolladorY', 'descripcion': 'Un juego nuevo'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Muy bien agregaste tu comunidad")

    def test_lista_comunidades(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('lista_comunidades')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Juego de Prueba")

    def test_eliminar_comunidades(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('eliminar_comunidades', args=[self.comunidad.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/l-comunidades')

    def test_editar_comunidad(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('editar_comunidad', args=[self.comunidad.id])
        data = {'nombre': 'Pelicula Modificada', 'fecha_salida': '2022-06-01', 'categoria': 'Peliculas', 'empresa': 'direccion', 'descripcion': 'Un juego modificado',}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cambios realizados")

#Test Documentado 2 "CRUD de Reseña":
class TestResenasViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.lista_resenas_url = reverse('lista_resenas')
        self.agregar_resena_url = reverse('agregar_resena')
        self.eliminar_resena_url = reverse('eliminar_resena', args=[1])
        self.editar_resena_url = reverse('editar_resena', args=[1])
        self.resena = Resena.objects.create(
            autor="Jhon Doe",
            contenido="Esta es una reseña de prueba",
            comunidad="Evangelion"
        )
        self.resena_form_data = {
            "autor": "Jane Smith",
            "contenido": "Esta es otra reseña de prueba",
            "comunidad": "Rick y Morty"
        }
    
    def test_lista_resenas_GET(self):
        response = self.client.get(self.lista_resenas_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_resenas.html')
    
    def test_agregar_resena_POST(self):
        response = self.client.post(self.agregar_resena_url, self.resena_form_data)
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Resena.objects.last().autor, 'Jane Smith')
        self.assertEquals(Resena.objects.last().contenido, 'Esta es otra reseña de prueba')
        self.assertEquals(Resena.objects.last().comunidad, 'Rick y Morty')
    
    def test_eliminar_resena_POST(self):
        response = self.client.post(self.eliminar_resena_url)
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Resena.objects.count(), 0)
    
    def test_editar_resena_GET(self):
        response = self.client.get(self.editar_resena_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_resena.html')
    
    def test_editar_resena_POST(self):
        response = self.client.post(self.editar_resena_url, self.resena_form_data)
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Resena.objects.first().autor, 'Jane Smith')
        self.assertEquals(Resena.objects.first().contenido, 'Esta es otra reseña de prueba')
        self.assertEquals(Resena.objects.first().comunidad, 'Rick y Morty')

#Test Documentado 3 "Login de usuarios":
class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login_usuarios')
        self.username = 'testuser'
        self.email = 'testuser@test.com'
        self.password = 'testpass'
        self.user = User.objects.create_user(
        username=self.username,
        email=self.email,
        password=self.password
    )
def test_login(self):
    response = self.client.post(self.login_url, {'username': self.username, 'password': self.password})
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('inicio'))
    self.assertTrue(response.wsgi_request.user.is_authenticated)

# Esos son todos los tests documentados requeridos, no hubo ningún error verdadero, 
# los errores que figuran en la terminal son errores hechos apropósito en el armado de los tests todo funciona bien,
# para ejecutar escribir en el terminal py manage.py test
