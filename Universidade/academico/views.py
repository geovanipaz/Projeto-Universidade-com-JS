from audioop import reverse
from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    return render(request, 'gestaoCursos.html',{'cursos':cursosListados})

def registrarCurso(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nome = request.POST['txtNombre']
        creditos = request.POST['numCreditos']
        
        curso = Curso.objects.create(
            codigo=codigo, nome=nome, creditos=creditos
        )
        curso.save()
        
        return redirect('/')
    
def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    return redirect('/')

def edicaoCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicaoCurso.html', {'curso':curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nome = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nome = nome
    curso.creditos = creditos
    
    curso.save()
    
    return redirect('/')