from django.contrib import admin


from apps.adopcion.models import Persona


@admin.register(Persona)
class adminMascota(admin.ModelAdmin):
    list_display=['nombre' , 'apellidos', 'edad', 'telefono', 'email', 'domicilio']
