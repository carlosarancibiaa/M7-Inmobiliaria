from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    tipos_usuarios = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador')
        ]
    
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    rut = models.CharField(max_length=10, primary_key=True)
    direccion= models.CharField(max_length=255, null=False)
    telefono = models.CharField(max_length=9, null=False)
    tipo = models.CharField(choices=tipos_usuarios, default='arrendador')
    
    def __str__(self):
        return f'''Nombre: {self.nombres} {self.apellidos}
        Rut: {self.rut}
        Tipo: {self.tipo}
        '''
    
class Comuna(models.Model):
    REGIONES_CHOICES = [
        ('XV', 'Región de Arica y Parinacota'),
        ('I', 'Región de Tarapacá'),
        ('II', 'Región de Antofagasta'),
        ('III', 'Región de Atacama'),
        ('IV', 'Región de Coquimbo'),
        ('V', 'Región de Valparaíso'),
        ('RM', 'Región Metropolitana de Santiago'),
        ('VI', "Región del Libertador General Bernardo O'Higgins"),
        ('VII', 'Región del Maule'),
        ('XVI', 'Región de Ñuble'),
        ('VIII', 'Región del Biobío'),
        ('IX', 'Región de La Araucanía'),
        ('XIV', 'Región de Los Ríos'),
        ('X', 'Región de Los Lagos'),
        ('XI', 'Región de Aysén del General Carlos Ibáñez del Campo'),
        ('XII', 'Región de Magallanes y de la Antártica Chilena')
    ]
    nombre = models.CharField(max_length=20, null=False)
    region = models.CharField(max_length=50, null=False, choices=REGIONES_CHOICES)
    
    def __str__(self):
        return f'''Nombre: {self.nombre}
        Región: {self.region}
        '''

class Inmueble(models.Model):
    tipos_inmueble = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela')
    ]
    
    nombre= models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=255, null=False)
    metros_construidos = models.IntegerField(null=False)
    metros_totales = models.IntegerField(null=False)
    cant_estacionamientos = models.SmallIntegerField(null=False)
    cant_habitaciones = models.SmallIntegerField(null=False)
    cant_baños = models.SmallIntegerField(null=False)
    direccion = models.CharField(max_length=255, null=False)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, related_name='inmuebles', null=False)
    tipo = models.CharField(choices=tipos_inmueble, default='casa')
    precio = models.IntegerField(null=False)
    dueño = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='propiedades')
    disponible = models.BooleanField(default=True)
    arrendatario = models.ForeignKey('Usuario', on_delete=models.SET_DEFAULT, default=None, related_name='propiedades_arrendadas', null=True)
    
    def __str__(self):
        if self.arrendatario:
            return f'''ID: {self.id}
            Direccion: {self.direccion}
            Comuna: {self.comuna.nombre}
            Region: {self.comuna.region}
            Dueño: {self.dueño.nombres} {self.dueño.apellidos   }
            Arrendatario: {self.arrendatario.nombres} {self.arrendatario.apellidos}
            Disponible: {self.disponible}
            '''
        else:
            return f'''ID: {self.id}
            Direccion: {self.direccion}
            Comuna: {self.comuna.nombre}
            Region: {self.comuna.region}
            Dueño: {self.dueño.nombres} {self.dueño.apellidos   }
            Arrendatario: {self.arrendatario}
            Disponible: {self.disponible}
            '''