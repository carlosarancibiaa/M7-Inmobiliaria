# Generated by Django 5.1 on 2024-09-03 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inmobiliaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='comuna',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='inmuebles', to='app_inmobiliaria.comuna'),
            preserve_default=False,
        ),
    ]
