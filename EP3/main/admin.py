from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Amostra)
admin.site.register(Exame)
admin.site.register(Possui)
admin.site.register(Outros_Dados_Amostra)
admin.site.register(Outros_Dados_Paciente)