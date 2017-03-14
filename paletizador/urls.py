from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^paletizador/$', views.paletizador_edit, name='edit'),
]
