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
    amostras = Amostra.objects.all().order_by("codigo")
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'amostras',
        'array' : amostras,
    }
    return HttpResponse(template.render(context, request))

def exame(request):
    exames = Exame.objects.all().order_by("codigo")
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'exames',
        'array' : exames,
    }
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
            'operacao' : 'inserir',
            'tipo' : 'paciente',
            'form' : form,
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
            'operacao' : 'inserir',
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
            'operacao' : 'inserir',
            'tipo' : 'exame',
            'form' : form
        }
        return HttpResponse(template.render(context, request))

def updatePaciente(request, paciente_id):
    paciente = Paciente.objects.get(pk = paciente_id)

    if request.method == 'POST':
        form = PacienteModelForm(request.POST, instance=paciente)
        form.save()
        return HttpResponseRedirect("../../paciente/")
    else: 
        form =  PacienteModelForm(instance=paciente)
        form.fields['cpf'].widget.attrs['readonly'] = True
        template = loader.get_template('form.html')

        context = {
                'operacao' : 'update',
                'tipo' : 'Paciente',
                'form' : form,
            }
        return HttpResponse(template.render(context, request))

def updateAmostra(request, amostra_id):
    amostra = Amostra.objects.get(pk = amostra_id)

    if request.method == 'POST':
        form = AmostraModelForm(request.POST, instance=amostra)
        form.save()
        return HttpResponseRedirect("../../amostra/")
    else: 
        form = AmostraModelForm(instance=amostra)
        form.fields['cpf'].widget.attrs['readonly'] = True
        template = loader.get_template('form.html')

        context = {
                'operacao' : 'update',
                'tipo' : 'amostra',
                'form' : form,
            }
        return HttpResponse(template.render(context, request))

def updateExame(request, exame_id):
    exame = Exame.objects.get(pk = exame_id)
    if request.method == 'POST':
        form = ExameModelForm(request.POST, instance=exame)
        form.save()
        return HttpResponseRedirect("../../exame/")
    else: 
        form = ExameModelForm(instance=exame)
        template = loader.get_template('form.html')

        context = {
                'operacao' : 'update',
                'tipo' : 'Exame',
                'form' : form
            }
        return HttpResponse(template.render(context, request))



def deletePaciente(request, paciente_id):
    paciente = Paciente.objects.get(pk = paciente_id)
    paciente.delete()
    return HttpResponseRedirect("../../paciente/")

def deleteAmostra(request, amostra_id):
    amostra = Amostra.objects.get(pk = amostra_id)
    amostra.delete()
    return HttpResponseRedirect("../../amostra/")

def deleteExame(request, exame_id):
    exame = Exame.objects.get(pk = exame_id)
    exame.delete()
    return HttpResponseRedirect("../../exame/")