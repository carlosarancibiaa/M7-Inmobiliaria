from .models import Usuario
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