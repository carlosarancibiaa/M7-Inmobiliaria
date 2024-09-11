# Generated by Django 5.1 on 2024-09-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inmobiliaria', '0004_alter_inmueble_arrendatario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='tipo',
            field=models.CharField(choices=[('casa', 'Casa'), ('departamento', 'Departamento'), ('parcela', 'Parcela')], default='casa', max_length=20),
        ),
    ]
