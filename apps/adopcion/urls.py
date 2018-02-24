from django.conf.urls import  url, include
from apps.adopcion.views import index

urlpatterns = [
        url(r'^$',index),
]
