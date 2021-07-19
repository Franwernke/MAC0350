from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paciente/', views.paciente, name='paciente'),
    path('amostra/', views.amostra, name='amostra'),
    path('exame/', views.exame, name='exame'),
    path('paciente/insert/', views.insertPaciente, name='insertPaciente'),
    path('amostra/insert/', views.insertAmostra, name='insertAmostra'),
    path('exame/insert/', views.insertExame, name='insertExame'),   
]