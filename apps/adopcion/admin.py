from django.contrib import admin


from apps.adopcion.models import Persona , Solicitud


@admin.register(Persona)
class adminPersona(admin.ModelAdmin):
    list_display=['nombre' , 'apellidos', 'edad', 'telefono', 'email', 'domicilio']

@admin.register(Solicitud)
class adminSolicitud(admin.ModelAdmin):
    list_display=['numero_mascotas' , 'razones']