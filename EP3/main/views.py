from django import template
from django.db.models.deletion import ProtectedError
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.http import HttpResponse
from .models import Amostra, Outros_Dados_Amostra, Paciente, Exame

from django.template import context, loader
from .forms import *

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def paciente(request):
    pacientes = Paciente.objects.all()
    outros_dados_paciente = Outros_Dados_Paciente.objects.all()

    pacientesComOutrosDados = []

    for paciente in pacientes:
        fields = paciente.get_fields()
        outros_dados = outros_dados_paciente.filter(cpf = paciente.cpf)
        outros_dados = outros_dados if len(outros_dados) != 0 else None
        pair = (fields, outros_dados)
        pacientesComOutrosDados.append(pair)
        
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'pacientes',
        'array' : pacientesComOutrosDados,
    }
    return HttpResponse(template.render(context, request))

def amostra(request):
    amostras = Amostra.objects.all().order_by("codigo")
    outros_dados_amostra = Outros_Dados_Amostra.objects.all()

    amostrasComOutrosDados = []

    for amostra in amostras:
        fields = amostra.get_fields()
        outros_dados = outros_dados_amostra.filter(codigo_amostra = amostra.codigo)
        outros_dados = outros_dados if len(outros_dados) != 0 else None
        pair = (fields, outros_dados)
        amostrasComOutrosDados.append(pair)

    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'amostras',
        'array' : amostrasComOutrosDados,
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

def possui(request):
    relation = Possui.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'possui',
        'array' : relation,
    }
    return HttpResponse(template.render(context, request))

def outros_dados_amostra(request):
    relation = Outros_Dados_Amostra.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'outros_dados_amostra',
        'array' : relation,
    }
    return HttpResponse(template.render(context, request))

def outros_dados_paciente(request):
    relation = Outros_Dados_Paciente.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'outros_dados_paciente',
        'array' : relation,
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

def insertPossui(request):
    if request.method == 'POST':
        result = ExameModelForm(request.POST)
        result.save()
        return HttpResponseRedirect("..")
    else:
        form = PossuiModelForm()
        template = loader.get_template('form.html')
        context = {
            'operacao' : 'inserir',
            'tipo' : 'possui',
            'form' : form
        }
        return HttpResponse(template.render(context, request))

def insertOutrosDadosPaciente(request, paciente_id):
    if request.method == 'POST':
        result = OutrosDadosPacienteModelForm(request.POST)
        result.save()
        return HttpResponseRedirect("../..")
    else:
        form = OutrosDadosPacienteModelForm()
        form.fields["cpf"].choices = ((paciente_id,paciente_id),)

        template = loader.get_template('form.html')
        context = {
            'operacao' : 'inserir',
            'tipo' : 'outros_dados_paciente',
            'form' : form
        }
        return HttpResponse(template.render(context, request))

def insertOutrosDadosAmostra(request, amostra_id):
    if request.method == 'POST':
        result = OutrosDadosAmostraModelForm(request.POST)
        result.save()
        return HttpResponseRedirect("../..")
    else:
        form = OutrosDadosAmostraModelForm()
        form.fields["codigo_amostra"].choices = ((amostra_id,amostra_id),)

        template = loader.get_template('form.html')
        context = {
            'operacao' : 'inserir',
            'tipo' : 'outros_dados_amostra',
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

def updatePossui(request, possui_id):
    possui = Possui.objects.get(pk = possui_id)
    if request.method == 'POST':
        form = PossuiModelForm(request.POST, instance=possui)
        form.save()
        return HttpResponseRedirect("../../possui/")
    else: 
        form = PossuiModelForm(instance=possui)
        template = loader.get_template('form.html')

        context = {
                'operacao' : 'update',
                'tipo' : 'Possui',
                'form' : form
            }
        return HttpResponse(template.render(context, request))

def updateOutrosDadosPaciente(request, outro_id):
    outros_dados_paciente = Outros_Dados_Paciente.objects.get(pk = outro_id)
    if request.method == 'POST':
        form = OutrosDadosPacienteModelForm(request.POST, instance=outros_dados_paciente)
        form.save()
        return HttpResponseRedirect("../..")
    else: 
        form = OutrosDadosPacienteModelForm(instance=outros_dados_paciente)
        form.fields["cpf"].choices = ((outros_dados_paciente.cpf.cpf, outros_dados_paciente.cpf.cpf),)
        

        template = loader.get_template('form.html')

        context = {
                'operacao' : 'update',
                'tipo' : 'OutrosDadosPaciente',
                'form' : form
            }
        return HttpResponse(template.render(context, request))

def updateOutrosDadosAmostra(request, outro_id):
    outros_dados_amostra = Outros_Dados_Amostra.objects.get(pk = outro_id)
    if request.method == 'POST':
        form = OutrosDadosAmostraModelForm(request.POST, instance=outros_dados_amostra)
        form.save()
        return HttpResponseRedirect("../..")
    else: 
        form = OutrosDadosAmostraModelForm(instance=outros_dados_amostra)
        form.fields["codigo_amostra"].choices = ((outros_dados_amostra.codigo_amostra.codigo, outros_dados_amostra.codigo_amostra.codigo),)

        template = loader.get_template('form.html')

        context = {
                'operacao' : 'update',
                'tipo' : 'OutrosDadosAmostra',
                'form' : form
            }
        return HttpResponse(template.render(context, request))


def deletePaciente(request, paciente_id):
    paciente = Paciente.objects.get(pk = paciente_id)
    try:
        paciente.delete()
    except(ProtectedError):
        return HttpResponseBadRequest("Este paciente é protegido pela restrição de chave estrangeira!<br>" + 
         "<a href=\"..\"> <button> Voltar </button> </a>")
    return HttpResponseRedirect("../../paciente/")

def deleteAmostra(request, amostra_id):
    amostra = Amostra.objects.get(pk = amostra_id)
    try:
        amostra.delete()
    except(ProtectedError):
        return HttpResponseBadRequest("Esta amostra é protegida pela restrição de chave estrangeira!<br>" + 
         "<a href=\"..\"> <button> Voltar </button> </a>")
    return HttpResponseRedirect("../../amostra/")

def deleteExame(request, exame_id):
    exame = Exame.objects.get(pk = exame_id)
    try:
        exame.delete()
    except(ProtectedError):
        return HttpResponseBadRequest("Este exame é protegido pela restrição de chave estrangeira!<br>" + 
         "<a href=\"..\"> <button> Voltar </button> </a>")
    return HttpResponseRedirect("../../exame/")

def deletePossui(request, possui_id):
    possui = Possui.objects.get(pk = possui_id)
    possui.delete()
    return HttpResponseRedirect("../../possui/")

def deleteOutrosDadosPaciente(request, outro_id):
    outros_dados_paciente = Outros_Dados_Paciente.objects.get(pk = outro_id)
    outros_dados_paciente.delete()
    return HttpResponseRedirect("../..")

def deleteOutrosDadosAmostra(request, outro_id):
    outros_dados_amostra = Outros_Dados_Amostra.objects.get(pk = outro_id)
    outros_dados_amostra.delete()
    return HttpResponseRedirect("../..")

def detailsPaciente(request, paciente_id):
    paciente = Paciente.objects.get(pk = paciente_id)
    amostras = Amostra.objects.filter(cpf = paciente.cpf)
    a = Possui.objects.filter(cpf = paciente.cpf)
    # print(exames)
    template = loader.get_template("detailsPaciente.html")
    context = {
        'paciente' : paciente,
        'amostras' : amostras,
        'exames' : a,
    }
    return HttpResponse(template.render(context, request))

def detailsAmostra(request, amostra_id):
    amostra = Amostra.objects.get(pk = amostra_id)
    context = {
        'amostra' : amostra
    }
    template = loader.get_template("detailsAmostra.html")
    return HttpResponse(template.render(context, request))

def detailsExame(request, exame_id):
    exame = Exame.objects.get(pk = exame_id)
    context = {
        'exame' : exame
    }
    template = loader.get_template("detailsExame.html")
    return HttpResponse(template.render(context, request))
