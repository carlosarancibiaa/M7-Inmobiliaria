from django.shortcuts import render, redirect, Http404
from .forms import FormRegistro, FormActualizacion, FormCreacionPropiedad
from django.contrib.auth import login,  authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comuna, Inmueble, Usuario
from .services import crear_inmueble, obtener_inmuebles, arrendar_inmueble, obtener_comunas

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
            return redirect('/profile')
    else:
        form=FormRegistro()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def perfil(request):
    a = request.POST.get('dueño')
    if request.method == 'POST':
        if request.POST.get('cancelar_arriendo'):
            print('holaaaas')
            p = Inmueble.objects.get(id=request.POST.get('cancelar_arriendo'))
            p.disponible=True
            p.arrendatario=None
            p.save()
            return redirect('/profile')
        propiedades= request.user.propiedades.all()
        agregar=True
        comunas = Comuna.objects.all()
        if a is not None:
            print('segundo post')
            dueño = Usuario.objects.get(rut=request.POST.get('dueño'))
            print(f'Dueño: {dueño}')
            i = Inmueble(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            metros_construidos=request.POST.get('metros_construidos'),
            metros_totales=request.POST.get('metros_totales'),
            cant_estacionamientos=request.POST.get('cant_estacionamientos'),
            cant_habitaciones=request.POST.get('cant_habitaciones'),
            cant_baños=request.POST.get('cant_baños'),
            direccion=request.POST.get('direccion'),
            comuna_id=request.POST.get('comuna'),
            tipo=request.POST.get('tipo'),
            precio=request.POST.get('precio'),
            dueño=dueño
            )
            i.save()
            agregar=False
        else:
            print('no hay dueño')
            
        return render(request, 'perfil.html', { 'comunas': comunas,'agregar':agregar, 'propiedades': propiedades})
    else:
        agregar= False
        propiedades= request.user.propiedades.all()
        propiedades_arrendadas = request.user.propiedades_arrendadas.all()
        return render(request, 'perfil.html', {'propiedades': propiedades,  'agregar':agregar, 'propiedades_arrendadas': propiedades_arrendadas})

@login_required
def actualizar(request):
    if request.method =='POST':
        form = FormActualizacion(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('/profile')
        else:
            print(form.errors)
            messages.error(request, 'Error en la actualización, por favor revise los campos.')
    else:
        form=FormActualizacion(instance=request.user)
    return render(request, 'actualizar.html', {'form': form})

@login_required
def crear_propiedades(request):
    propiedades= request.user.propiedades.all()
    try:
        if request.method =='POST':
            form = FormCreacionPropiedad(request.POST)
            if form.is_valid():
                try:
                    inmueble = form.save(commit=False)
                    inmueble.dueño = request.user
                    inmueble.save()
                    messages.success(request, 'Inmueble agregado correctamente.')
                    return redirect('/properties')
                except Exception as e:
                    messages.error(request, f'Error al guardar la propiedad: {e}')
        else:
            form = FormCreacionPropiedad()
    except Exception as e:
        print(e)
        
    return render(request, 'crear_propiedades.html', {'form': form, 'inmuebles': propiedades})

@login_required
def propiedades(request):
    if request.user.tipo == 'arrendador':
        if request.method == 'POST' and request.POST.get('id_eliminar'):
            Inmueble.objects.get(id=request.POST['id_eliminar']).delete()
        propiedades = obtener_inmuebles(rut=request.user.rut)
    else:
        if request.method == 'POST' and request.POST.get('id_arrendar'):
            propiedades = obtener_inmuebles(disponible=True)
            arrendar_inmueble(request.user.rut, request.POST['id_arrendar'])     
        elif request.method == 'POST' and request.POST.get('filtro_region'):
            propiedades = Inmueble.objects.filter(comuna__region = request.POST['filtro_region'], disponible=True)
        elif request.method == 'POST' and request.POST.get('filtro_comuna'):
            propiedades = Inmueble.objects.filter(comuna = request.POST['filtro_comuna'], disponible=True)
        else:
            propiedades = obtener_inmuebles(disponible=True)
    comunas = obtener_comunas()
    regiones = Comuna.objects.values('region').distinct()
    return render(request, 'propiedades.html', {'inmuebles': propiedades, 'comunas':comunas, 'regiones':regiones})

@login_required
def actualizar_propiedades(request):
    inmuebles = obtener_inmuebles(rut=request.user.rut)
    if request.method == 'POST'and request.POST.get('id_actualizar'):
        inmueble = Inmueble.objects.get(id=request.POST['id_actualizar'])
        form = FormCreacionPropiedad()
        return render(request, 'actualizar_propiedades.html', {'inmueble': inmueble, 'inmuebles': inmuebles, 'form': form})
    elif request.method == 'POST'and request.POST['id_confirmar']:
        inmueble = Inmueble.objects.get(id=request.POST['id_confirmar'])
        try:
            formulario = FormCreacionPropiedad(request.POST, instance=inmueble)
            if formulario.is_valid():
                formulario.save()
                return redirect('properties')
            else:
                print('else', formulario.errors)
        except Exception as e:
            print(e)
    return render(request, 'actualizar_propiedades.html', {'inmuebles': inmuebles})
    