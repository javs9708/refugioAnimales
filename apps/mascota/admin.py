from django.contrib import admin

from apps.mascota.models import Vacuna,Mascota

@admin.register(Mascota)
class adminMascota(admin.ModelAdmin):
	list_display = ['nombre' , 'sexo' , 'edad' , 'fecha_rescate' , 'persona']

@admin.register(Vacuna)
class adminMascota(admin.ModelAdmin):
    list_display=['nombre']
