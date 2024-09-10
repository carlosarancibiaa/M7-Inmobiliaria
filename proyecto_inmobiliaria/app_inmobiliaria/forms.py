from .models import Usuario, Inmueble
from django import forms
from django.contrib.auth.forms import UserCreationForm

class FormRegistro(UserCreationForm):
    
    tipo = forms.ChoiceField(choices=Usuario.tipos_usuarios)
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'tipo', 'email', 'password1', 'password2' ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'rut': 'Rut',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'tipo': 'Tipo',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Repetir Contraseña'
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        rut = self.cleaned_data.get('rut')
        user.username = rut  # Asigna el RUT al campo username
        user.rut = rut  # Guarda también el RUT en el campo rut
        if commit:
            user.save()
        return user
    
class FormActualizacion(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'direccion', 'telefono','email']
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'email': 'Correo electrónico',
        }
        
class FormCreacionPropiedad(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'direccion', 'comuna', 'metros_construidos', 'metros_totales','cant_estacionamientos', 'cant_habitaciones', 'cant_baños', 'tipo', 'precio' ]
        labels ={
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'direccion': 'Direccion',
            'comuna': 'Comuna',
            'metros_construidos': 'Metros contruidos',
            'metros_totales': 'Metros totales',
            'cant_estacionamientos': 'Estacionamientos' ,
            'cant_habitaciones': 'Habitaciones',
            'cant_baños': 'Baños',
            'tipo': 'Tipo',
            'precio': 'Precio'    
        }