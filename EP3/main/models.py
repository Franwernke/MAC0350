from django.db import models

class Paciente(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return "Nome: " + self.nome + " Cpf: " + self.cpf

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Exame(models.Model):
    codigo = models.AutoField(primary_key=True)
    virus = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    data_de_solicitacao = models.DateTimeField()
    data_de_execucao = models.DateTimeField()
    #cpfs = models.ManyToOneRel(Paciente, through='Possui')
    
    def __str__(self):
        return "Codigo: " + str(self.codigo) + " Virus: " + self.virus + " Tipo: " + self.tipo
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Outros_Dados_Paciente(models.Model):
    dado = models.CharField(max_length=255)
    cpf = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Amostra(models.Model):
    codigo = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11)
    data_de_coleta = models.DateTimeField()
    tipo_de_material = models.CharField(max_length=255)
    #cpfs = models.ManyToOneRel(Paciente, through='Possui')
    #codigos_exames = models.ManyToManyField(Exame, through='Possui')

    def __str__(self):
        return "Codigo: " + str(self.codigo) + " cpf: " + self.cpf + " Tipo de Material: " + self.tipo_de_material
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Outros_Dados_Amostra(models.Model):
    dado = models.CharField(max_length=255)
    codigo_amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
    def __str__(self):
        return "dado: " + str(self.dado)

class Outros_Dados_Paciente(models.Model):
    dado = models.CharField(max_length=255)
    cpf = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
    def __str__(self):
        return "dado: " + str(self.dado) 


class Possui(models.Model):
    cpf = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    codigo_exame = models.ForeignKey(Exame, on_delete=models.PROTECT)
    codigo_amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE, null=True, blank = True)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['cpf', 'codigo_exame', 'codigo_amostra'], name='unique_exame_amostra')
                ]
    
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
    def __str__(self):
        cpf = self.cpf.cpf
        codigo_exame = self.codigo_exame.codigo

        if (self.codigo_amostra == None):
            codigo_amostra = "ainda não foi coletada nenhuma amostra."
        else:
            codigo_amostra = self.codigo_amostra.codigo
        return "cpf: " + str(cpf)  + " Exame: " + str(codigo_exame)+ " Amostra: " + str(codigo_amostra)
