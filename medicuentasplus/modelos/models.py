from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from fernet_fields import EncryptedTextField

class CustomUser(AbstractUser):
    especialidad = models.CharField(max_length=200, blank=True)
    departamento = models.CharField(max_length=200, blank=True)


#Aqui empieza todo

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=1000, blank=True, null=True)

class Ciudad(models.Model):
    ciudad = models.CharField(max_length=1000, blank=True, null=True)

class Usuario(models.Model):
    primernombre = models.CharField(max_length=1000, blank=True, null=True)
    segundonombre = models.CharField(max_length=1000, blank=True, null=True)
    primerapellido = models.CharField(max_length=1000, blank=True, null=True)
    segundoapellido = models.CharField(max_length=1000, blank=True, null=True)
    usuario = models.CharField(max_length=1000, blank=True, null=True)
    clave = models.TextField(blank=True, null=True)
    tipodocumento= models.CharField(max_length=1000, blank=True, null=True)
    numerodocumento= models.CharField(max_length=1000, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    edad = models.CharField(max_length=100, blank=True, null=True)
    numerotelefono = models.IntegerField( blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE,blank=True, null=True) 
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE,blank=True, null=True) 
    rol = models.CharField(max_length=500, blank=True , null=True)
    asistente = models.CharField(max_length=500, blank=True, null= True)
    permisoscomentario = models.CharField(max_length=100, blank=True, null= True)
    sexo = models.CharField(max_length=500, blank=True, null= True)
    consultorio = models.CharField(max_length=500, blank=True, null= True)
    estado = models.CharField(max_length=500, blank=True, null= True)

class Entidad(models.Model):
    entidad = models.CharField(max_length=1000, blank=True, null=True)

class Paciente(models.Model):
    nombres = models.CharField(max_length=1000, blank=True, null=True)
    apellidos = models.CharField(max_length=1000, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField( blank=True, null=True)
    sexo = models.CharField(max_length=500, blank=True, null= True)
    telefono = models.CharField(max_length=500, blank=True, null= True)
    tipodocumento= models.CharField(max_length=1000, blank=True, null=True)
    numerodocumento = models.CharField(max_length=500, blank=True, null= True)
    movil = models.CharField(max_length=500, blank=True, null= True)
    correo = models.CharField(max_length=500, blank=True, null= True)

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True,null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE,blank=True, null=True) 
    especialista = models.ForeignKey(Usuario, on_delete=models.CASCADE,blank=True, null=True) 
    actividad = models.TextField(blank=True, null=True)
    fechacita = models.DateField(blank=True, null=True)
    horacita = models.TimeField(blank=True, null=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE,blank=True, null=True) 
    clasecita = models.CharField(max_length=1000, blank=True, null=True)


class HistoriasClinica(models.Model):
    paciente =  models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True,null=True)


class Diagnostico(models.Model):
    codigo = models.CharField(max_length=1000, blank=True, null=True)
    diagnostico = models.CharField(max_length=1000, blank=True, null=True)    

class Consulta(models.Model):
    historiaclinicas = models.ForeignKey(HistoriasClinica, on_delete=models.CASCADE, blank=True,null=True)
    fechaconsulta = models.DateField(blank=True, null=True)
    fechaalta = models.TimeField(blank=True, null=True)
    diagnostico = models.CharField(max_length=1000, blank=True, null=True)
    tratamiento = models.TextField(blank=True, null=True)
    otrosdatos = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

