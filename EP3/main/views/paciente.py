from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import loader
from main.forms import OutrosDadosPacienteModelForm, PacienteModelForm
from ..models import Amostra, Outros_Dados_Paciente, Paciente, Possui
from django.db.models.deletion import ProtectedError

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

def detailsPaciente(request, paciente_id):
    paciente = Paciente.objects.get(pk = paciente_id)
    amostras = Amostra.objects.filter(cpf = paciente.cpf)
    a = Possui.objects.filter(cpf = paciente.cpf)
    template = loader.get_template("detailsPaciente.html")
    context = {
        'paciente' : paciente,
        'amostras' : amostras,
        'exames' : a,
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


def outros_dados_paciente(request):
    relation = Outros_Dados_Paciente.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'outros_dados_paciente',
        'array' : relation,
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

def deleteOutrosDadosPaciente(request, outro_id):
    outros_dados_paciente = Outros_Dados_Paciente.objects.get(pk = outro_id)
    outros_dados_paciente.delete()
    return HttpResponseRedirect("../..")

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
