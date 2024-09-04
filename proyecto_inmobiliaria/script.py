import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmobiliaria.settings')
django.setup()

from app_inmobiliaria.models import Inmueble

def obtener_inmuebles_comunas(palabra=None):
    if palabra==None:
        consulta = Inmueble.objects.all().order_by('comuna')
    else:
        consulta =  Inmueble.objects.filter(Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra)).order_by('comuna')
    with open('inmuebles_por_comuna.txt', 'w') as i:
        for c in consulta:
            i.write(str(c)+'\n')
    print('Archivo inmuebles por comuna escrito exitosamente!')

def obtener_inmuebles_regiones():
    consulta = Inmueble.objects.all().order_by('comuna__region')
    with open('inmuebles_por_region.txt', 'w') as i:
        for c in consulta:
            i.write(str(c)+'\n')
    print('Archivo inmuebles por region escrito exitosamente!')
    
if __name__ == '__main__':
    obtener_inmuebles_comunas()
    obtener_inmuebles_regiones()
    print('Archivos escritos exitosamente')
