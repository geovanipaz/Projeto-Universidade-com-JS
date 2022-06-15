from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicaoCurso/<codigo>', views.edicaoCurso, name='edicao_curso'),
    path('editarCurso/', views.editarCurso, name='editar_curso'),
    path('eliminarCurso/<codigo>', views.eliminarCurso, name='eliminar_curso')
]
