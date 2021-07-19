from django import forms

class PacienteForm(forms.Form):
    cpf = forms.CharField(max_length=11)
    nome = forms.CharField(max_length=255)
    endereco = forms.CharField(max_length=255)
    data_de_nascimento = forms.DateField()

""" class Exame(forms.Form):
    codigo = forms.AutoField(primary_key=True)
    virus = forms.CharField(max_length=255)
    tipo = forms.CharField(max_length=255)
    data_de_solicitacao = forms.DateTimeField()
    data_de_execucao = forms.DateTimeField()
    #cpfs = forms.ManyToOneRel(Paciente, through='Possui')
    
    def __str__(self):
        return "Codigo: " + str(self.codigo) + " Virus: " + self.virus + " Tipo: " + self.tipo

class Outros_Dados_Paciente(forms.Form):
    dado = forms.CharField(max_length=255)
    cpf = forms.ForeignKey(Paciente, on_delete=forms.PROTECT)

class Amostra(forms.Form):
    codigo = forms.AutoField(primary_key=True)
    cpf = forms.CharField(max_length=11)
    data_de_coleta = forms.DateTimeField()
    tipo_de_material = forms.CharField(max_length=255)
    #cpfs = forms.ManyToOneRel(Paciente, through='Possui')
    codigos_exames = forms.ManyToManyField(Exame, through='Possui')

    def __str__(self):
        return "Codigo: " + str(self.codigo) + " cpf: " + self.cpf + " Tipo de Material: " + self.tipo_de_material

class Outros_Dados_Amostra(forms.Form):
    dado = forms.CharField(max_length=255)
    codigo_amostra = forms.ForeignKey(Amostra, on_delete=forms.PROTECT)

class Possui(forms.Form):
    cpf = forms.ForeignKey(Paciente, on_delete=forms.PROTECT)
    codigo_exame = forms.ForeignKey(Exame, on_delete=forms.PROTECT)
    codigo_amostra = forms.ForeignKey(Amostra, on_delete=forms.PROTECT, null=True)
 """