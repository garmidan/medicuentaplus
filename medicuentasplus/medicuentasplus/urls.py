"""medicuentasplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from modelos.views import cambiocontraseñausuario,dashboard, login, cambiocontraseña, bloquearobservaciones, historialviewpdf, eliminarcita, deleteentidad, entidad, registrarcitapacienteregister,edithistori, editarhistoriaclinica, logout, usuarios, guardarhistoriaclinica, verhistoriaclinica, historiaclinica, registarprestador,historialregistrar, citas, registracita, especialidadseleccionada, citasdetalles, editarusuarios, inactivarusuario, registarasistente, maestros,especialidades, deleteespecialidades, deleteciudades, ciudades
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('administrador', admin.site.urls),
    path('', login),
    path('dashboard',dashboard),
    path('logout',logout),
    path('usuarios',usuarios),
    path('usuarios/registrarprestador', registarprestador),
    path('usuarios/registarasistente', registarasistente),
    path('citas',citas),
    path('citas/registrarcita',registracita),
    path('citas/registrarcitas',registrarcitapacienteregister),
    path('citas/detalles/<str:prestador>',citasdetalles),
    path('usuarios/editar/<int:iduser>',editarusuarios),
    path('usuarios/inactivar/activar/<int:idusuario>',inactivarusuario),
    path('especialidadseleccionada', especialidadseleccionada, name="especialidadseleccionada"),
    path('maestros',maestros),
    path('maestros/especialidades',especialidades),
    path('maestros/especialidades/<int:idespecialidad>',deleteespecialidades),
    path('maestros/entidad/<int:identidad>',deleteentidad),
    path('maestros/ciudades',ciudades),
    path('maestros/entidades',entidad),
    path('maestros/ciudades/<int:idciudad>',deleteciudades),
    path('historiasclinicas/historialregistrarconsulta/<int:idhistoria>',historialregistrar),
    path('historiasclinicas/detallehistoria/<int:id>',verhistoriaclinica),
    path('historiasclinicas',historiaclinica),
    path('historiasclinicas/view',historialviewpdf, name="historiasclinicas/view"),
    path('historiasclinicas/nuevahistoria/<int:idpaciente>',guardarhistoriaclinica),
    path('historiasclinicas/editarhistoriaclinica/<int:idhis>',editarhistoriaclinica),
    path('historiasclinicas/editarhistoriaclinicasa/<int:id1>/<int:id2>',edithistori),
    path('cancelarcita/<int:id1citas>',eliminarcita),
    path('bloqueo/<str:asis>',bloquearobservaciones),
    path('cambiocontraseña/<int:iduser>',cambiocontraseña),
    path('cambiocontraseñausuario',cambiocontraseñausuario),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

