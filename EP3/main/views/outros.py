from django.http.response import HttpResponseRedirect
from django.http import HttpResponse

from django.template import loader
from ..forms import *

def possui(request):
    relation = Possui.objects.all()
    template = loader.get_template('listAll.html')
    context = {
        'titulo' : 'possui',
        'array' : relation,
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

def deletePossui(request, possui_id):
    possui = Possui.objects.get(pk = possui_id)
    possui.delete()
    return HttpResponseRedirect("../../possui/")