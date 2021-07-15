from django.db import models


class Paciente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()

class Exame(models.Model):
    codigo = models.IntegerField()
    virus = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    data_de_solicitacao = models.DateTimeField()
    data_de_execucao = models.DateTimeField()
    #cpfs = models.ManyToOneRel(Paciente, through='Possui')

class Outros_Dados_Paciente(models.Model):
    dado = models.CharField(max_length=255)
    cpf = models.ForeignKey(Paciente, on_delete=models.PROTECT)

class Amostra(models.Model):
    codigo = models.IntegerField()
    cpf = models.CharField(max_length=11)
    data_de_coleta = models.DateTimeField()
    tipo_de_material = models.DateTimeField()
    #cpfs = models.ManyToOneRel(Paciente, through='Possui')
    codigos_exames = models.ManyToManyField(Exame, through='Possui')

class Outros_Dados_Amostra(models.Model):
    dado = models.CharField(max_length=255)
    codigo_amostra = models.ForeignKey(Amostra, on_delete=models.PROTECT)


class Possui(models.Model):
    cpf = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    codigo_exame = models.ForeignKey(Exame, on_delete=models.PROTECT)
    codigo_amostra = models.ForeignKey(Amostra, on_delete=models.PROTECT)