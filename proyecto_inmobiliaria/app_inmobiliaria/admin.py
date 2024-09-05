from django.contrib import admin
from .models import Usuario, Comuna, Inmueble

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Comuna)
admin.site.register(Inmueble)