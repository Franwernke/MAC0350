from django.forms import ModelForm
from .models import *

class PacienteModelForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['cpf', 'nome', 'endereco', 'data_de_nascimento']

class AmostraModelForm(ModelForm):
    class Meta:
        model = Amostra
        fields = ['codigo','cpf', 'data_de_coleta', 'tipo_de_material']

class ExameModelForm(ModelForm):
    class Meta:
        model = Exame
        fields = ['codigo', 'virus', 'tipo', 'data_de_solicitacao', 'data_de_execucao']

class PossuiModelForm(ModelForm):
    class Meta:
        model = Possui
        fields = ['cpf', 'codigo_exame', 'codigo_amostra']

class OutrosDadosAmostraModelForm(ModelForm):
    class Meta:
        model = Outros_Dados_Amostra
        fields = ['dado', 'codigo_amostra']

class OutrosDadosPacienteModelForm(ModelForm):
    class Meta:
        model = Outros_Dados_Paciente
        fields = ['dado', 'cpf']