# Generated by Django 3.2.5 on 2021-07-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_amostra_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amostra',
            name='cpf',
        ),
        migrations.AddField(
            model_name='amostra',
            name='cpf',
            field=models.ManyToManyField(through='main.Possui', to='main.Paciente'),
        ),
    ]
