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
   
    path('paciente/update/<paciente_id>', views.updatePaciente, name='updatePaciente'),
    path('amostra/update/<amostra_id>', views.updateAmostra, name='updateAmostra'),
    path('exame/update/<exame_id>', views.updateExame, name='updateExame'),


    path('paciente/delete/<paciente_id>', views.deletePaciente, name='deletePaciente'),
    path('amostra/delete/<amostra_id>', views.deleteAmostra, name='deleteAmostra'),
    path('exame/delete/<exame_id>', views.deleteExame, name='deleteExame'),
]