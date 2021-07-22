from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import loader
from main.forms import ExameModelForm
from ..models import Exame
from django.db.models.deletion import ProtectedError

def exame(request):
    exames = Exame.objects.all().order_by("codigo")
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'exames',
        'array' : exames,
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

def deleteExame(request, exame_id):
    exame = Exame.objects.get(pk = exame_id)
    try:
        exame.delete()
    except(ProtectedError):
        return HttpResponseBadRequest("Este exame é protegido pela restrição de chave estrangeira!<br>" + 
         "<a href=\"..\"> <button> Voltar </button> </a>")
    return HttpResponseRedirect("../../exame/")

def detailsExame(request, exame_id):
    exame = Exame.objects.get(pk = exame_id)
    context = {
        'exame' : exame
    }
    template = loader.get_template("detailsExame.html")
    return HttpResponse(template.render(context, request))
