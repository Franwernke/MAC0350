# Generated by Django 3.2.5 on 2021-07-16 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_amostra_tipo_de_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outros_dados_amostra',
            name='codigo_amostra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.amostra', unique=True),
        ),
        migrations.AlterField(
            model_name='outros_dados_paciente',
            name='cpf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.paciente', unique=True),
        ),
    ]
