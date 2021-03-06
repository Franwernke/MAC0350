from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import loader
from main.forms import AmostraModelForm, OutrosDadosAmostraModelForm, PossuiModelForm
from ..models import Amostra, Outros_Dados_Amostra, Possui, Exame
from django.db.models.deletion import ProtectedError

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

def detailsAmostra(request, amostra_id):
    amostra = Amostra.objects.get(pk = amostra_id)
    posse = Possui.objects.filter(codigo_amostra = amostra_id).order_by("codigo_exame")
    exames = []

    paciente = posse.first().cpf

    for possui in posse:
        codigo_exame = possui.codigo_exame.codigo
        exame = Exame.objects.get(pk = codigo_exame)

        if len(exames) == 0 or exames[-1] != exame:
            exames.append(exame)

    context = {
        'paciente' : paciente,
        'amostra' : amostra,
        'exames': exames,
    }
    template = loader.get_template("detailsAmostra.html")
    return HttpResponse(template.render(context, request))

def insertAmostra(request):
    if request.method == 'POST':
        result = AmostraModelForm(request.POST)
        result.save()
        return HttpResponseRedirect(str(Amostra.objects.last().codigo))
    else:
        form = AmostraModelForm()
        template = loader.get_template('form.html')
        context = {
            'operacao' : 'inserir',
            'tipo' : 'amostra',
            'form' : form
        }
        return HttpResponse(template.render(context, request))
    
def insertAmostraExame(request, amostra_id):
    cpf = Amostra.objects.get(pk = amostra_id).cpf

    if request.method == 'POST':
        result = PossuiModelForm(request.POST)
        result.save()

        posse = Possui.objects.order_by("id")
        codigo_exame = posse.last().codigo_exame.codigo
        posse = posse.filter(codigo_exame = codigo_exame)

        if posse.count() == 2 and posse.first().codigo_amostra == None:
            posse.first().delete()

        return HttpResponseRedirect("../" + str(amostra_id))
    else:
        
        posse = Possui.objects.filter(cpf = cpf).order_by("codigo_exame")
        exames = []

        for possui in posse:
            codigo_exame = possui.codigo_exame.codigo
            exame = Exame.objects.get(pk = codigo_exame)

            if len(exames) == 0 or exames[-1][0] != exame.codigo:
                exames.append((exame.codigo, exame.codigo))

        form = PossuiModelForm()    
        form.fields["codigo_amostra"].choices = ((amostra_id,amostra_id),)
        form.fields["cpf"].choices = ((cpf, cpf),)
        form.fields['codigo_exame'].choices = tuple(exames)

        template = loader.get_template('form.html')
        context = {
            'operacao' : 'Escolha um',
            'tipo' : 'exame',
            'form' : form
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

def deleteAmostra(request, amostra_id):
    amostra = Amostra.objects.get(pk = amostra_id)

    posse = Possui.objects.filter(codigo_amostra = amostra_id).order_by("codigo_exame")

    for possui in posse:
        if (Possui.objects.filter(codigo_exame = possui.codigo_exame.codigo).count() == 1):
            possui.codigo_amostra = None
            possui.save()

    try:
        amostra.delete()
    except(ProtectedError):
        return HttpResponseBadRequest("Esta amostra ?? protegida pela restri????o de chave estrangeira!<br>" + 
         "<a href=\"..\"> <button> Voltar </button> </a>")
    return HttpResponseRedirect("../../amostra/")

def outros_dados_amostra(request):
    relation = Outros_Dados_Amostra.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'outros_dados_amostra',
        'array' : relation,
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

def deleteOutrosDadosAmostra(request, outro_id):
    outros_dados_amostra = Outros_Dados_Amostra.objects.get(pk = outro_id)
    outros_dados_amostra.delete()
    return HttpResponseRedirect("../..")

def amostraRedirect(request, amostra_id):
    return HttpResponseRedirect(".")