from django.shortcuts import render
from django.http import HttpResponse
#from .models import Usuario
#from .models import Perfil
from django.db import connection
from collections import namedtuple
from django.template import loader

def index(request):
    return HttpResponse("MAC0350: EP3")
    
def query1(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ep3_usuario')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('query1.html')
    context = {'query1_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def query2(request):
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT u.nome, u.login, u.cpf, string_agg(p.tipo, \', \') as perfis FROM ep3_usuario as u\
                LEFT JOIN ep3_usuario_possui_perfil as possui\
                ON u.id = possui.usuario_id\
                JOIN ep3_perfil as p\
                ON possui.perfil_id = p.id\
                GROUP BY u.nome, u.login, u.cpf\
                ')
        result = named_tuple_fetchall(cursor)
    print(result)
    template = loader.get_template('query2.html')
    context = {'query2_result_list': result,}
    
    return HttpResponse(template.render(context, request))
#metodos auxiliares

def named_tuple_fetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    result = [nt_result(*row) for row in cursor.fetchall()]

    return result
