from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paciente/', views.paciente, name='paciente'),
    path('amostra/', views.amostra, name='amostra'),
    path('exame/', views.exame, name='exame'),
    path('possui/', views.possui, name='possui'),
    path('outrosDadosAmostra/', views.outros_dados_amostra, name='outrosDadosAmostra'),
    path('outrosDadosPaciente/', views.outros_dados_paciente, name='outrosDadosPaciente'),

    path('paciente/insert/', views.insertPaciente, name='insertPaciente'),
    path('amostra/insert/', views.insertAmostra, name='insertAmostra'),
    path('exame/insert/', views.insertExame, name='insertExame'),
    path('possui/insert/', views.insertPossui, name='insertPossui'),

    path('paciente/update/<paciente_id>', views.updatePaciente, name='updatePaciente'),
    path('amostra/update/<amostra_id>', views.updateAmostra, name='updateAmostra'),
    path('exame/update/<exame_id>', views.updateExame, name='updateExame'),
    path('possui/update/<possui_id>', views.updatePossui, name='updatePossui'),

    path('paciente/delete/<paciente_id>', views.deletePaciente, name='deletePaciente'),
    path('amostra/delete/<amostra_id>', views.deleteAmostra, name='deleteAmostra'),
    path('exame/delete/<exame_id>', views.deleteExame, name='deleteExame'),
    path('possui/delete/<possui_id>', views.deletePossui, name='deletePossui'),

    path('paciente/other/insert/<paciente_id>', views.insertOutrosDadosPaciente, name='insertOutrosDadosPaciente'),
    path('amostra/other/insert/<amostra_id>', views.insertOutrosDadosAmostra, name='insertOutrosDadosAmostra'),

    path('paciente/other/delete/<outro_id>', views.deleteOutrosDadosPaciente, name='updateOutrosDadosPaciente'),
    path('amostra/other/delete/<outro_id>', views.deleteOutrosDadosAmostra, name='updateOutrosDadosAmostra'),

    path('paciente/other/update/<outro_id>', views.updateOutrosDadosPaciente, name='updateOutrosDadosPaciente'),
    path('amostra/other/update/<outro_id>', views.updateOutrosDadosAmostra, name='updateOutrosDadosAmostra'),
]