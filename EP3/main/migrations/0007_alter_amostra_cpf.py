# Generated by Django 3.2.5 on 2021-07-22 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_possui_codigo_amostra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='cpf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.paciente'),
        ),
    ]
