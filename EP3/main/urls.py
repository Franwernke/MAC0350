from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paciente/', views.paciente, name='paciente'),
    path('amostra/', views.amostra, name='amostra'),
    path('amostra/<amostra_id>', views.amostraRedirect, name='amostraID'),
    path('exame/', views.exame, name='exame'),
    path('possui/', views.possui, name='possui'),
    path('outrosDadosAmostra/', views.outros_dados_amostra, name='outrosDadosAmostra'),
    path('outrosDadosPaciente/', views.outros_dados_paciente, name='outrosDadosPaciente'),

    path('paciente/insert/', views.insertPaciente, name='insertPaciente'),
    path('amostra/insert/', views.insertAmostra, name='insertAmostra'),
    path('amostra/insert/<amostra_id>', views.insertAmostraExame, name='insertAmostraExame'),

    path('exame/insert/', views.insertExame, name='insertExame'),
    path('exame/insert/<exame_id>', views.insertExamePaciente, name='insertExamePaciente'),
    path('possui/insert/', views.insertPossui, name='insertPossui'),

    path('paciente/update/<paciente_id>', views.updatePaciente, name='updatePaciente'),
    path('amostra/update/<amostra_id>', views.updateAmostra, name='updateAmostra'),
    path('exame/update/<exame_id>', views.updateExame, name='updateExame'),
    path('possui/update/<possui_id>', views.updatePossui, name='updatePossui'),

    path('paciente/delete/<paciente_id>', views.deletePaciente, name='deletePaciente'),
    path('amostra/delete/<amostra_id>', views.deleteAmostra, name='deleteAmostra'),
    path('exame/delete/<exame_id>', views.deleteExame, name='deleteExame'),
    path('possui/delete/<possui_id>', views.deletePossui, name='deletePossui'),

    path('paciente/details/<paciente_id>', views.detailsPaciente, name='detailsPaciente'),
    path('paciente/details/', lambda req: redirect('..')),
    path('amostra/details/<amostra_id>', views.detailsAmostra, name='detailsAmostra'),
    path('amostra/details/insert/<amostra_id>', views.insertAmostraExame, name='detailsInsertAmostraExame'),
    path('amostra/details/', lambda req: redirect('..')),
    path('exame/details/<exame_id>', views.detailsExame, name='detailsExame'),
    path('exame/details/', lambda req: redirect('..')),

    path('paciente/other/insert/<paciente_id>', views.insertOutrosDadosPaciente, name='insertOutrosDadosPaciente'),
    path('amostra/other/insert/<amostra_id>', views.insertOutrosDadosAmostra, name='insertOutrosDadosAmostra'),

    path('paciente/other/delete/<outro_id>', views.deleteOutrosDadosPaciente, name='updateOutrosDadosPaciente'),
    path('amostra/other/delete/<outro_id>', views.deleteOutrosDadosAmostra, name='updateOutrosDadosAmostra'),

    path('paciente/other/update/<outro_id>', views.updateOutrosDadosPaciente, name='updateOutrosDadosPaciente'),
    path('amostra/other/update/<outro_id>', views.updateOutrosDadosAmostra, name='updateOutrosDadosAmostra'),
    
    path('paciente/other/', lambda req: redirect('..')),
    path('amostra/other/', lambda req: redirect('..')),
]