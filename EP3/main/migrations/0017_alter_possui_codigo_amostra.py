# Generated by Django 3.2.5 on 2021-07-22 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210722_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possui',
            name='codigo_amostra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.amostra'),
        ),
    ]