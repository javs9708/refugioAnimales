
from django.conf.urls import  url, include
from apps.mascota.views import *


urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^nuevo$',MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^vacuna$',vacuna_view, name='vacuna_crear'),
    url(r'^listar$',MascotaList.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/$',mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$',mascota_delete, name='mascota_eliminar'),

]
