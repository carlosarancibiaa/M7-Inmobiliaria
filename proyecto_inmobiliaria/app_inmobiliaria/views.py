from django.shortcuts import render, redirect
from .forms import FormRegistro
from django.contrib.auth import login,  authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            usuario_autenticado = form.save()
            rut = form.cleaned_data.get('rut')
            contraseña = form.cleaned_data.get('password1')
            usuario_autenticado = authenticate(username=rut, password=contraseña)
            login(request, usuario_autenticado)
            return redirect('/')
    else:
        form=FormRegistro()
    return render(request, 'registration/register.html', {'form': form})