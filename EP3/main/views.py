from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template.base import constant_string
from .models import Amostra, Outros_Dados_Amostra, Paciente, Exame
from django.db import connection
from collections import namedtuple
from django.template import context, loader
from .forms import *

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def paciente(request):
    pacientes = Paciente.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'pacientes',
        'array' : pacientes,
    }
    return HttpResponse(template.render(context, request))

def amostra(request):
    amostras = Amostra.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'amostras',
        'array' : amostras,
    }
    return HttpResponse(template.render(context, request))

def exame(request):
    exames = Exame.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'exames',
        'array' : exames,
    }
    return HttpResponse(template.render(context, request))

def form(request):
    
    if request.method == 'POST':
        form = PacienteForm(request.POST)
    else:
        form = PacienteForm()
        #attrs = [str(i)[14:] for i in Paciente._meta.fields]
    
    template = loader.get_template('form.html')
    context = {
        'form': form,
        'tipo' : 'paciente', 
        #'attrs' : attrs,
    }
    print(type(request))
    
    return HttpResponse(template.render(context, request))


def insertPaciente(request):
    if request.method == 'POST':
        result = PacienteModelForm(request.POST)
        result.save()
        return HttpResponseRedirect("..")
    else:
        form = PacienteModelForm()
        template = loader.get_template('form.html')
        context = {
            'tipo' : 'paciente',
            'form' : form
        }
        return HttpResponse(template.render(context, request))

def insertAmostra(request):
    if request.method == 'POST':
        result = AmostraModelForm(request.POST)
        result.save()
        return HttpResponseRedirect("..")
    else:
        form = AmostraModelForm()
        template = loader.get_template('form.html')
        context = {
            'tipo' : 'amostra',
            'form' : form
        }
        return HttpResponse(template.render(context, request))

def insertExame(request):
    if request.method == 'POST':
        result = ExameModelForm(request.POST)
        result.save()
        return HttpResponseRedirect("..")
    else:
        form = ExameModelForm()
        template = loader.get_template('form.html')
        context = {
            'tipo' : 'exame',
            'form' : form
        }
        return HttpResponse(template.render(context, request))

# def query1(request):
#     with connection.cursor() as cursor:
#         cursor.execute('SELECT * FROM ep3_usuario')
#         result = named_tuple_fetchall(cursor)
    
#     template = loader.get_template('query1.html')
#     context = {'query1_result_list': result,}
    
#     return HttpResponse(template.render(context, request))

# def query2(request):
#     with connection.cursor() as cursor:
#         cursor.execute('\
#                 SELECT u.nome, u.login, u.cpf, string_agg(p.tipo, \', \') as perfis FROM ep3_usuario as u\
#                 LEFT JOIN ep3_usuario_possui_perfil as possui\
#                 ON u.id = possui.usuario_id\
#                 JOIN ep3_perfil as p\
#                 ON possui.perfil_id = p.id\
#                 GROUP BY u.nome, u.login, u.cpf\
#                 ')
#         result = named_tuple_fetchall(cursor)
#     print(result)
#     template = loader.get_template('query2.html')
#     context = {'query2_result_list': result,}
    
#     return HttpResponse(template.render(context, request))
# #metodos auxiliares

# def named_tuple_fetchall(cursor):
#     desc = cursor.description
#     nt_result = namedtuple('Result', [col[0] for col in desc])
#     result = [nt_result(*row) for row in cursor.fetchall()]

#     return result
