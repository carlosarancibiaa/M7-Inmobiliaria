from .models import Usuario, Inmueble, Comuna

def crear_usuario(nombres:str, apellidos:str, rut:str, direccion:str, telefono:str, tipo:str = 'arrendador'):
    Usuario(username=rut, nombres=nombres, apellidos=apellidos, rut=rut, direccion=direccion, telefono=telefono, tipo=tipo).save()
    
def crear_inmueble(nombre:str, descripcion:str, metros_construidos:int, metros_totales:int, cant_estacionamientos:int, cant_habitaciones:int, cant_baños:int, direccion:str, id_comuna:int, tipo:str, precio:int, dueño:str, disponible:bool, arrendatario:str = None):
    
    comuna = Comuna.objects.get(id=id_comuna)
    dueño = Usuario.objects.get(rut=dueño)
    if arrendatario:
        arrendatario= Usuario.objects.get(rut=arrendatario)
        disponible=False
    else:
        disponible = True
        
    Inmueble(nombre=nombre,descripcion=descripcion,metros_construidos=metros_construidos,metros_totales=metros_totales,cant_estacionamientos=cant_estacionamientos, cant_habitaciones=cant_habitaciones, cant_baños=cant_baños, direccion=direccion,comuna=comuna,tipo=tipo, precio=precio, dueño=dueño, disponible=disponible, arrendatario=arrendatario).save()
    
def crear_comuna(nombre=None, region=None):
    try:
        Comuna.objects.get_or_create(nombre=nombre, region=region)
    except Exception as e:
        print(f'Error al crear las comunas: {e}')
    
def obtener_usuario(rut:str):
    try:
        return Usuario.objects.get(rut=rut)
    except Exception as e:
        print(f'Error al obtener el usuario: {e}')

def obtener_comunas():
    return Comuna.objects.all()
    
def obtener_inmuebles(rut=None, disponible=None):
    if rut is None and disponible is None:
        return Inmueble.objects.all()
    elif disponible is None:
        return Inmueble.objects.filter(dueño=rut)
    return Inmueble.objects.filter(disponible=disponible)
    

def arrendar_inmueble(arrendatario:str, id_inmueble:int):
    arrendatario=Usuario.objects.get(rut=arrendatario)
    inmueble = Inmueble.objects.get(id=id_inmueble)
    inmueble.arrendatario = arrendatario
    inmueble.disponible = False
    inmueble.save()

def eliminar_inmueble(id):
    try:
        Inmueble.objects.get(id=id).delete()
    except Exception as e:
        print(f'Error al eliminar inmueble: {e}')
        