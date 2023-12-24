from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    try: 
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'inicio.html', {'url': avatar.imagen.url})
    except:
        return render(request, "inicio.html")
    
def AboutMe(request):
    return render(request, "aboutme.html")
    
#1er Círculo Inicio!!
@login_required   
def agregar_comunidad(request):
    if request.method == 'POST':
        mi_formulario = ComunidadesForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            comunidad = Comunidad(nombre=request.POST['nombre'], fecha_salida=request.POST['fecha_salida'], categoria=request.POST['categoria'], empresa=request.POST['empresa'], descripcion=request.POST['descripcion'],)
            comunidad.save()
            return render(request, "inicio.html", {"mensaje": "Muy bien agregaste tu comunidad :D"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = ComunidadesForm()
        return render(request, "agregar_comunidad.html", {"mi_formulario": mi_formulario})

@login_required  
def lista_comunidad(request):
    orden = request.GET.get('orden', None)
    comunidades = Comunidad.objects.all()
    if orden == 'lanzamiento':
        comunidades = comunidades.order_by('-fecha_salida')
    elif orden == 'valoracion':
        comunidades = comunidades.order_by('-valoracion')
    return render(request, "ver_comunidades.html", {"comunidades": comunidades})

@login_required
def eliminar_comunidades(request, id):
    if request.method == 'POST':
        comunidad = Comunidad.objects.get(id=id)
        comunidad.delete()
        comunidad = Comunidad.objects.all()
        return HttpResponseRedirect('/l-comunidades')

@login_required    
def editar_comunidades(request, id):
    comunidad = Comunidad.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = ComunidadesForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            comunidad.nombre = data['nombre']
            comunidad.fecha_salida = data['fecha_salida']
            comunidad.categoria = data['categoria']
            comunidad.empresa = data['empresa']
            comunidad.descripcion = data['descripcion']
            comunidad.valoracion = data['valoracion']
            comunidad.save()
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = ComunidadesForm(initial={
            "nombre": comunidad.nombre,
            "fecha_salida": comunidad.fecha_salida,
            "categoria": comunidad.categoria,
            "empresa": comunidad.empresa,
            "descripcion": comunidad.descripcion,
        })
        return render(request, "editar_Comunidades.html", {"mi_formulario": mi_formulario, "id": comunidad.id})

@login_required    
def agregar_resena(request):
    mi_formulario = ResenaForm()
    if request.method == 'POST':
        mi_formulario = ResenaForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return HttpResponseRedirect('/l-resenas')
    return render(request, 'agregar_resena.html', {'mi_formulario': mi_formulario})

@login_required
def lista_resenas(request):
    resenas = Resena.objects.all()
    return render(request, 'lista_resenas.html', {'reseñas': resenas})

@login_required
def eliminar_resena(request, id):
    if request.method == 'POST':
        resena = Resena.objects.get(id=id)
        resena.delete()
        resena = Resena.objects.all()
        return HttpResponseRedirect('/l-resenas')

login_required    
def editar_resena(request, id):
    resena = Resena.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = ResenaForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            resena.autor = data['autor']
            resena.contenido = data['contenido']
            resena.comunidad = data['comunidad']
            resena.save()
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = ResenaForm(initial={
            "autor": resena.autor,
            "contenido": resena.contenido,
            "comunidad": resena.comunidad,
        })
        return render(request, "editar_resena.html", {"mi_formulario": mi_formulario, "id": resena.id})
#1er Círculo Fin!!

#2do Círculo Inicio!!
@login_required
def busqueda_comunidades(request):
    return render(request, 'buscar_comunidades.html')

@login_required
def buscar_nombre(request):
    if request.method == 'GET':
        form = BuscarNombre(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            comunidades = Comunidad.objects.filter(nombre__icontains=nombre)
            return render(request, 'res_busqueda_nombre.html', {'comunidades': comunidades, 'nombre': nombre})
    else:
        form = BuscarNombre()
    return render(request, 'busq_nombre.html', {'form': form})

@login_required
def buscar_categoria(request):
    if request.method == 'GET':
        form = BuscarCategoria(request.GET)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            comunidades = Comunidad.objects.filter(categoria__icontains=categoria)
            return render(request, 'res_busqueda_categoria.html', {'comunidades': comunidades, 'categoria': categoria})
    else:
        form = BuscarCategoria()
    return render(request, 'busq_categoria.html', {'form': form})

@login_required
def buscar_empresa(request):
    if request.method == 'GET':
        form = BuscarEmpresa(request.GET)
        if form.is_valid():
            empresa = form.cleaned_data['empresa']
            comunidades = Comunidad.objects.filter(empresa__icontains=empresa)
            return render(request, 'res_busqueda_empresa.html', {'comunidades': comunidades, 'empresa': empresa})
    else:
        form = BuscarEmpresa()
    return render(request, 'busq_empresa.html', {'form': form})

@login_required
def buscar_valoracion(request):
    if request.method == 'GET':
        form = BuscarValoracion(request.GET)
        if form.is_valid():
            valoracion = form.cleaned_data['valoracion']
            comunidades = Comunidad.objects.filter(valoracion__icontains=valoracion)
            return render(request, 'res_busqueda_valoracion.html', {'comunidades': comunidades, 'valoracion': valoracion})
    else:
        form = BuscarValoracion()
    return render(request, 'busq_valoracion.html', {'form': form})
#2do Cícurlo Final!!

#3er Círculo Inicio!!
@login_required
def lista_temas(request):
    temas = Tema.objects.all()
    return render(request, 'foro.html', {'temas': temas})

@login_required
def crear_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save(commit=False)
            tema.creador = request.user
            tema.save()
            return HttpResponseRedirect('/foro')
    else:
        form = TemaForm()
    return render(request, 'crear_tema.html', {'form': form})

@login_required
def editar_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    if request.method == 'POST':
        form = TemaForm(request.POST, instance=tema)
        if form.is_valid():
            tema = form.save()
            return HttpResponseRedirect('/foro')
    else:
        form = TemaForm(instance=tema)
    return render(request, 'editar_tema.html', {'form': form, 'tema': tema})

@login_required
def eliminar_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    tema.delete()
    return HttpResponseRedirect('/foro')

@login_required
def detalle_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    comentarios = Comentario.objects.filter(tema=tema)
    form = ComentarioForm()
    return render(request, 'detalle_tema.html', {'tema': tema, 'comentarios': comentarios, 'form': form})

@login_required
def crear_comentario(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.creador = request.user
            comentario.tema = tema
            comentario.save()
            return HttpResponseRedirect(reverse('DetalleTema', args=[tema.pk]))
    else:
        form = ComentarioForm()
    return render(request, 'crear_comentario.html', {'form': form})
#3er Círculo Final

#El 4to Círculo está en AppMensajes