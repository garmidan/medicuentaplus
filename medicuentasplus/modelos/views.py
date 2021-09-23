from django.shortcuts import render, redirect
from cryptography.fernet import Fernet
from modelos.models import Usuario, Especialidad, Ciudad, Cita, Entidad, HistoriasClinica, Paciente, Consulta
import base64
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse 
from datetime import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def dashboard(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            usuario = Usuario.objects.get(id=request.session.get('user'))
            prestador = {}
            if usuario.rol == "Asistente":

                prestador = Usuario.objects.get(asistente=usuario.primernombre+"-"+usuario.usuario)
            return render(request,'dashboard.html',{"usuario":usuario,"sesion":request.session.get('validar'),"prestador":prestador})
        else:
            return redirect('/')
        

def login(request):
    validar = 0
    print(request.session.get('validar'))
    if request.method == 'POST':
        if Usuario.objects.filter(usuario = request.POST.get("email")).exists():
            usuario = Usuario.objects.get(usuario=request.POST.get("email"))
            clave = request.POST.get("clave")
            base64_message = usuario.clave
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            if clave == message:
                if usuario.estado == "Activo":
                    if usuario.rol == "Asistente":
                        if Usuario.objects.filter(asistente=usuario.primernombre+"-"+usuario.usuario).exists():
                            request.session['validar'] = True
                            request.session['user'] = usuario.id
                            return redirect('/dashboard')
                        else:
                            validar = 3
                            return render(request,'login.html',{"validar":validar,"sesion":request.session.get('validar')})
                    elif usuario.rol != "Asistente":
                        request.session['validar'] = True
                        request.session['user'] = usuario.id
                        return redirect('/dashboard')
                else:
                    validar = 2
                    return render(request,'login.html',{"validar":validar,"sesion":request.session.get('validar')})
            else:
                validar = 1
                return render(request,'login.html',{"validar":validar,"sesion":request.session.get('validar')})
        else:
            validar = 1
            return render(request,'login.html',{"validar":validar,"sesion":request.session.get('validar')})
    return render(request,'login.html',{"sesion":request.session.get('validar')})

def logout(request):
    request.session['validar'] = False
    print(request.session.get('validar'))
    request.session['user'] = 0
    return render(request,'login.html',{"sesion":request.session.get('validar')})

def usuarios(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            usuarios = Usuario.objects.all()
            return render(request,'miusuarios.html',{"usuarios":usuarios,"usuario":usuario,"sesion":request.session.get('validar')})
        else:
            return redirect('/dashboard')

def registarprestador(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        validar = 0
        asistentes = []
        asistente = []
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            if Usuario.objects.filter(rol="Asistente").exists():
                asistente = Usuario.objects.filter(rol="Asistente")
                for asi in asistente:
                    if Usuario.objects.filter(asistente=asi.primernombre+"-"+asi.usuario).exists():
                        print("Si tiene prestador"+asi.primernombre)
                    else:
                        asistentes.append(asi.primernombre+"-"+asi.usuario)
            especialidad = Especialidad.objects.all()
            ciudad = Ciudad.objects.all()
            tipodocumento = ["CEDULA DE CIUDADANIA","CEDULA DE EXTRANJERIA","TARJETA DE IDENTIDAD","REGISTRO CIVIL","PASAPORTE","MENOR SIN IDENTIFICACION","ADULTO SIN IDENTIDAD"]
            sexo = ["MASCULINO","FEMENINO"]
            if request.method == 'POST':
                if Usuario.objects.filter(usuario = request.POST.get("correo")).exists() or Usuario.objects.filter(numerodocumento = request.POST.get("numerodoc")).exists():
                    validar = 2
                    return render(request,'prestador.html',{"usuario":usuario,"asistentes":asistentes,"especialidad":especialidad,"ciudad":ciudad,"tipodocumento":tipodocumento,"sexo":sexo,"sesion":request.session.get('validar'),"validar":validar})
                ciudadselcect = Ciudad.objects.get(id=request.POST.get("ciudad"))
                especialidadselect = Especialidad.objects.get(id=request.POST.get("especialidad"))
                clave = request.POST.get("clave")
                message_bytes = clave.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                usuario = Usuario(
                    primernombre = request.POST.get("primerN"),
                    segundonombre = request.POST.get("segundoN"),
                    primerapellido = request.POST.get("primerA"),
                    segundoapellido = request.POST.get("segundoA"),
                    usuario = request.POST.get("correo"),
                    clave = base64_message,
                    tipodocumento = request.POST.get("tipdoc"),
                    numerodocumento = request.POST.get("numerodoc"),
                    fechanacimiento = request.POST.get("fecha"),
                    sexo = request.POST.get("sexo"),
                    numerotelefono = request.POST.get("telefono"),
                    ciudad = ciudadselcect,
                    especialidad = especialidadselect,
                    rol = "Prestador",
                    asistente = request.POST.get("asistente"),
                    permisoscomentario = "Si",
                    consultorio = request.POST.get("consultorio"),
                    estado = "Activo"
                )
                usuario.save()
                validar = 1
            #mystr_encoded = base64.b64encode(mystr.encode('utf-8'))
            return render(request,'prestador.html',{"usuario":usuario,"asistentes":asistentes,"especialidad":especialidad,"ciudad":ciudad,"tipodocumento":tipodocumento,"sexo":sexo,"sesion":request.session.get('validar'),"validar":validar})
        else:
            return redirect('/dashboard')
        

def registarasistente(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        validar = 0 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            ciudad = Ciudad.objects.all()
            tipodocumento = ["CEDULA DE CIUDADANIA","CEDULA DE EXTRANJERIA","TARJETA DE IDENTIDAD","REGISTRO CIVIL","PASAPORTE","MENOR SIN IDENTIFICACION","ADULTO SIN IDENTIDAD"]
            sexo = ["MASCULINO","FEMENINO"]
            if request.method == "POST":
                if Usuario.objects.filter(usuario = request.POST.get("correo")).exists() or Usuario.objects.filter(numerodocumento = request.POST.get("numerodoc")).exists():
                    validar = 2
                    return render(request,'asistente.html',{"usuario":usuario,"ciudad":ciudad,"tipodocumento":tipodocumento,"sexo":sexo,"sesion":request.session.get('validar'),"validar":validar})
                ciudadselcect = Ciudad.objects.get(id=request.POST.get("ciudad"))
                clave = request.POST.get("clave")
                message_bytes = clave.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                usuario = Usuario(
                    primernombre = request.POST.get("primerN"),
                    segundonombre = request.POST.get("segundoN"),
                    primerapellido = request.POST.get("primerA"),
                    segundoapellido = request.POST.get("segundoA"),
                    usuario = request.POST.get("correo"),
                    clave = base64_message,
                    tipodocumento = request.POST.get("tipdoc"),
                    numerodocumento = request.POST.get("numerodoc"),
                    fechanacimiento = request.POST.get("fecha"),
                    sexo = request.POST.get("sexo"),
                    numerotelefono = request.POST.get("telefono"),
                    ciudad = ciudadselcect,
                    rol = "Asistente",
                    permisoscomentario = "Si",
                    estado = "Activo"
                    )
                usuario.save()
                validar = 1
            return render(request,'asistente.html',{"usuario":usuario,"ciudad":ciudad,"tipodocumento":tipodocumento,"sexo":sexo,"sesion":request.session.get('validar'),"validar":validar})
        else:
            return redirect('/dashboard')

def citas(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        citas = []
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Asistente" or usuario.rol == "Prestador":
            if Usuario.objects.filter(asistente=usuario.primernombre+"-"+usuario.usuario).exists():
                consulta = Usuario.objects.get(asistente=usuario.primernombre+"-"+usuario.usuario)
            else:
                consulta = usuario
            print(consulta)
            especialidad = Especialidad.objects.all()
            clasecita = ["PRIMERA VEZ","CONTROL"]
            sexo = ["MASCULINO","FEMENINO"]
            entidad = Entidad.objects.all()
            tipodocumento = ["CEDULA DE CIUDADANIA","CEDULA DE EXTRANJERIA","TARJETA DE IDENTIDAD","REGISTRO CIVIL","PASAPORTE","MENOR SIN IDENTIFICACION","ADULTO SIN IDENTIDAD"]
            if request.method == "POST":
                if Paciente.objects.filter(numerodocumento=request.POST.get("numerodocumento")).exists():
                    pacientico = Paciente.objects.get(numerodocumento=request.POST.get("numerodocumento"))
                    return render(request,'registrarpacientecita.html',{"sexo":sexo,"usuario":usuario,"paciente":pacientico,"especialidad":especialidad,"entidad":entidad,"clasecita":clasecita})
                else:
                    numerodocu = request.POST.get("numerodocumento")
                    return render(request,'registrarcitas.html',{"sexo":sexo,"usuario":usuario,"especialidad":especialidad,"entidad":entidad,"tipodocumento":tipodocumento,"clasecita":clasecita,"numerodoc":numerodocu,"sesion":request.session.get('validar')})
            if Cita.objects.filter(especialista = consulta).exists():
                citas = Cita.objects.filter(especialista = consulta)
                return render(request,'citas.html',{"usuario":usuario,"citasagendadas":citas,"sesion":request.session.get('validar')})
            else:
                return render(request,'citas.html',{"usuario":usuario,"citasagendadas":citas,"sesion":request.session.get('validar')})
        else:
            prestador = Usuario.objects.filter(rol = "Prestador")
            if request.method == "POST":
                especialidad = Especialidad.objects.all()
                clasecita = ["PRIMERA VEZ","CONTROL"]
                sexo = ["MASCULINO","FEMENINO"]
                entidad = Entidad.objects.all()
                tipodocumento = ["CEDULA DE CIUDADANIA","CEDULA DE EXTRANJERIA","TARJETA DE IDENTIDAD","REGISTRO CIVIL","PASAPORTE","MENOR SIN IDENTIFICACION","ADULTO SIN IDENTIDAD"]
                if Paciente.objects.filter(numerodocumento=request.POST.get("numerodocumento")).exists():
                    pacientico = Paciente.objects.get(numerodocumento=request.POST.get("numerodocumento"))
                    return render(request,'registrarpacientecita.html',{"sexo":sexo,"tipodocumento":tipodocumento,"usuario":usuario,"paciente":pacientico,"especialidad":especialidad,"entidad":entidad,"clasecita":clasecita,"sesion":request.session.get('validar')})
                else:
                    numerodocu = request.POST.get("numerodocumento")
                    return render(request,'registrarcitas.html',{"sexo":sexo,"usuario":usuario,"especialidad":especialidad,"entidad":entidad,"tipodocumento":tipodocumento,"clasecita":clasecita,"numerodoc":numerodocu,"sesion":request.session.get('validar')})
            return render(request,'citas.html',{"prestador":prestador,"usuario":usuario})

def registrarcitapacienteregister(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            usuario = Usuario.objects.get(id=request.session.get('user'))
            validar = 0
            if request.method == "POST":
                paciente = Paciente.objects.get(numerodocumento=request.POST.get("numerodocumentico"))
                if usuario.rol == "Asistente":
                    especialistaselect = Usuario.objects.get(asistente=usuario.primernombre+"-"+usuario.usuario)
                    especialidadselect = especialistaselect.especialidad
                elif usuario.rol == "Prestador":
                    especialistaselect = usuario
                    especialidadselect = usuario.especialidad
                else:
                    especialidadselect = Especialidad.objects.get(id=request.POST.get("especialidad"))
                    especialistaselect = Usuario.objects.get(id=request.POST.get("selectprestador"))
                entidadselect = Entidad.objects.get(id=request.POST.get("entidad"))
                paciente.nombres = request.POST.get("nombres")
                paciente.apellidos = request.POST.get("apellidos")
                if request.POST.get("fechanacimiento"):
                    paciente.fechanacimiento = request.POST.get("fechanacimiento")
                    paciente.edad = request.POST.get("edad")
                paciente.sexo = request.POST.get("sexo")
                paciente.numerodocumento = request.POST.get("numerodoc")
                paciente.telefono = request.POST.get("telefono")
                paciente.movil = request.POST.get("movil")
                paciente.correo = request.POST.get("correo")
                paciente.tipodocumento = request.POST.get("tipodoc")
                paciente.save()
                editpaciente = Paciente.objects.last()
                agendarcita = Cita(
                        paciente = editpaciente,
                        especialidad = especialidadselect,
                        especialista = especialistaselect,
                        actividad =  request.POST.get("actividad"),
                        fechacita = request.POST.get("fechacita"),
                        horacita = request.POST.get("horacita"),
                        clasecita = request.POST.get("clasecita"),
                        entidad = entidadselect
                )
                agendarcita.save()
                validar = 1
            return render(request,'registrarpacientecita.html',{"validar":validar,"paciente":paciente,"usuario":usuario,"sesion":request.session.get('validar')})
        else:
            return redirect('/')

def registracita(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        usuario = Usuario.objects.get(id=request.session.get('user'))
        validar = 0 
        especialidad = Especialidad.objects.all()
        entidad = Entidad.objects.all()
        tipodocumento = ["CEDULA DE CIUDADANIA","CEDULA DE EXTRANJERIA","TARJETA DE IDENTIDAD","REGISTRO CIVIL","PASAPORTE","MENOR SIN IDENTIFICACION","ADULTO SIN IDENTIDAD"]
        clasecita = ["PRIMERA VEZ","CONTROL"]
        if request.method == 'POST':
            if usuario.rol == "Asistente":
                especialistaselect = Usuario.objects.get(asistente=usuario.primernombre+"-"+usuario.usuario)
                especialidadselect = especialistaselect.especialidad
            elif usuario.rol == "Prestador":
                especialistaselect = usuario
                especialidadselect = usuario.especialidad
            else:
                especialidadselect = Especialidad.objects.get(id=request.POST.get("especialidad"))
                especialistaselect = Usuario.objects.get(id=request.POST.get("selectprestador"))
            entidadselect = Entidad.objects.get(id=request.POST.get("entidad"))
            pacienteregi = Paciente(
                nombres = request.POST.get("nombres"),
                apellidos = request.POST.get("apellidos"),
                fechanacimiento = request.POST.get("fechanacimiento"),
                edad = request.POST.get("edad"),
                sexo = request.POST.get("sexo"),
                numerodocumento = request.POST.get("numerodoc"),
                telefono = request.POST.get("telefono"),
                movil = request.POST.get("movil"),
                correo = request.POST.get("correo"),
                tipodocumento = request.POST.get("tipodoc")
            )
            pacienteregi.save()
            ultimoregistropaciente = Paciente.objects.last()
            agendarcita = Cita(
                paciente = ultimoregistropaciente,
                especialidad = especialidadselect,
                especialista = especialistaselect,
                actividad =  request.POST.get("actividad"),
                fechacita = request.POST.get("fechacita"),
                horacita = request.POST.get("horacita"),
                clasecita = request.POST.get("clasecita"),
                entidad = entidadselect
            )
            agendarcita.save()
            validar = 1
        return render(request,'registrarcitas.html',{"usuario":usuario,"especialidad":especialidad,"entidad":entidad,"tipodocumento":tipodocumento,"clasecita":clasecita,"validar":validar,"sesion":request.session.get('validar')})

@csrf_exempt
def especialidadseleccionada(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        if request.method == 'POST':
            usuario = Usuario.objects.get(id=request.session.get('user'))
            selectespe =  request.POST.get("selectespe")
            especialida = Especialidad.objects.get(id=selectespe)
            prestadore = Usuario.objects.filter(especialidad=especialida).values()
            print(selectespe)
            return JsonResponse({
                "success": True,
                "prestadores":list(prestadore)
            })

def citasdetalles(request,prestador):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        if Usuario.objects.filter(numerodocumento = prestador).exists():
            usuario = Usuario.objects.get(id=request.session.get('user'))
            especialistadetalle = Usuario.objects.get(numerodocumento=prestador)
            if Cita.objects.filter(especialista = especialistadetalle).exists():
                citasdetalles = Cita.objects.filter(especialista = especialistadetalle)
                return render(request,"citasdetalles.html",{"prestadordetalle":citasdetalles,"usuario":usuario,"sesion":request.session.get('validar')})
            else:
                return render(request,"citasdetalles.html",{"usuario":usuario,"sesion":request.session.get('validar')})

def inactivarusuario(request,idusuario):
    user = Usuario.objects.get(id=idusuario)
    if user.estado == "Activo":
        user.estado = "Inactivo"
        user.save()
    else:
        user.estado = "Activo"
        user.save()
    return redirect('/usuarios')

def editarusuarios(request, iduser):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            asistente = []
            asistentes = []
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if usuario.rol == "Administrador":
                tipodocumento = ["CEDULA DE CIUDADANIA","CEDULA DE EXTRANJERIA","TARJETA DE IDENTIDAD","REGISTRO CIVIL","PASAPORTE","MENOR SIN IDENTIFICACION","ADULTO SIN IDENTIDAD"]
                sexo = ["MASCULINO","FEMENINO"]
                if request.method == "POST":
                    editusuario = Usuario.objects.get(id=iduser)
                    editusuario.segundonombre = request.POST.get("segundoN")
                    editusuario.primerapellido = request.POST.get("primerA")
                    editusuario.segundoapellido = request.POST.get("segundoA")
                    editusuario.tipodocumento = request.POST.get("tipdoc")
                    editusuario.sexo = request.POST.get("sexo")
                    editusuario.telefono = request.POST.get("telefono")
                    editusuario.numerodocumento = request.POST.get("numerodoc")
                    ciudad = Ciudad.objects.get(id = request.POST.get("ciudad"))
                    editusuario.ciudad = ciudad
                    if editusuario.rol == "Prestador":
                        especialidad = Especialidad.objects.get(id = request.POST.get("especialidad"))
                        editusuario.especialidad = especialidad
                        editusuario.consultorio = request.POST.get("consultorio")
                        editusuario.asistente = request.POST.get("asistente")
                    elif editusuario.rol == "Asistente":
                        if Usuario.objects.filter(asistente=editusuario.primernombre+"-"+editusuario.usuario).exists():
                            pres = Usuario.objects.get(asistente=editusuario.primernombre+"-"+editusuario.usuario)
                            pres.asistente = request.POST.get("primerN")+"-"+request.POST.get("correo")
                            pres.save()
                    editusuario.primernombre = request.POST.get("primerN")
                    editusuario.usuario = request.POST.get("correo")
                    editusuario.save()
                    return redirect('/usuarios')
                else:     
                    if Usuario.objects.filter(rol="Asistente").exists():
                        asistente = Usuario.objects.filter(rol="Asistente")
                        for asi in asistente:
                            if Usuario.objects.filter(asistente=asi.primernombre+"-"+asi.usuario).exists():
                                print("")
                            else:
                                asistentes.append(asi.primernombre+"-"+asi.usuario)
                    print(asistentes)
                    asistente = Usuario.objects.filter(rol="Asistente")
                    print(asistente.count())
                    especialidad = Especialidad.objects.all()
                    ciudad = Ciudad.objects.all()
                    useredit = Usuario.objects.get(id=iduser)
                    return render(request,"editarusuarios.html",{"usuario":usuario,"useredit":useredit,"asistente":asistentes,"especialidad":especialidad,"ciudad":ciudad,"tipodocumento":tipodocumento,"sexo":sexo,"sesion":request.session.get('validar')})
            else:
                return redirect('/dashboard')
        else:
            return redirect('/')

def maestros(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            return render(request,"maestros.html",{"usuario":usuario,"sesion":request.session.get('validar')})
        else:
            return redirect('/dashboard')
    

def especialidades(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            especialidades = Especialidad.objects.all()
            validar = 0
            if request.method == "POST":
                especiaregister = Especialidad(especialidad=request.POST.get("especialidad"))
                especiaregister.save()
                validar = 1
            return render(request,"especialidad.html",{"usuario":usuario,"especialidades":especialidades,"validar":validar,"sesion":request.session.get('validar')})
        else:
            return redirect('/dashboard')

def deleteespecialidades(request,idespecialidad):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            deleteespe = Especialidad.objects.get(id=idespecialidad)
            deleteespe.delete()
            return redirect('/maestros/especialidades')
        else:
            return redirect('/dashboard')

def entidad(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            entidades = Entidad.objects.all()
            validar = 0
            if request.method == "POST":
                entidadregister = Entidad(entidad=request.POST.get("entidad"))
                entidadregister.save()
                validar = 1
            return render(request,"entidades.html",{"usuario":usuario,"entidades":entidades,"validar":validar,"sesion":request.session.get('validar')})
        else:
            return redirect('/dashboard')

def deleteentidad(request,identidad):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            deleteentidad = Entidad.objects.get(id=identidad)
            deleteentidad.delete()
            return redirect('/maestros/entidades')
        else:
            return redirect('/dashboard')

def ciudades(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            ciudades = Ciudad.objects.all()
            validar = 0
            if request.method == "POST":
                ciudadregister = Ciudad(ciudad=request.POST.get("ciudad"))
                ciudadregister.save()
                validar = 1
            return render(request,"ciudades.html",{"usuario":usuario,"ciudades":ciudades,"validar":validar,"sesion":request.session.get('validar')})
        else:
            return redirect('/dashboard')

def deleteciudades(request,idciudad):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        usuario = Usuario.objects.get(id=request.session.get('user'))
        if usuario.rol == "Administrador":
            deleteciudad = Ciudad.objects.get(id=idciudad)
            deleteciudad.delete()
            return redirect('/maestros/ciudades')
        else:
            return redirect('/dashboard')

def guardarhistoriaclinica(request,idpaciente):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if usuario.rol == "Administrador" or usuario.rol == "Prestador":
                if request.method == "POST":
                    pacientico = Paciente.objects.get(id=idpaciente)
                    historiaclinicare = HistoriasClinica(
                        paciente= pacientico
                    )
                    historiaclinicare.save()
                    print("Historia registrada")
                    ultimoregistro = HistoriasClinica.objects.last()
                    consultaregister = Consulta(
                    historiaclinicas = ultimoregistro,
                    fechaconsulta = request.POST.get("fechaconsulta"),
                    fechaalta = request.POST.get("horaconsulta"),
                    diagnostico = request.POST.get("diagnostico"),
                    tratamiento = request.POST.get("tratamiento"),
                    otrosdatos = request.POST.get("otrosdatos"),
                    observaciones = request.POST.get("observaciones")
                    )
                    consultaregister.save()
                    print("Consulta registrada")
                return render(request,"nuevahistoria.html",{"usuario":usuario,"sesion":request.session.get('validar')})
            else:
                return redirect('/dashboard')
        else:
            return redirect('/')
    

def historiaclinica(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            usuario = Usuario.objects.get(id=request.session.get('user'))
            validacion = 0
            pacientes = Paciente.objects.all()
            paciente = Paciente.objects.all()
            historiaclinica = HistoriasClinica.objects.all()
            if request.method == "POST":
                if Paciente.objects.filter(numerodocumento=request.POST.get("numerodocumento")).exists():
                    paciente = Paciente.objects.get(numerodocumento=request.POST.get("numerodocumento"))
                    if HistoriasClinica.objects.filter(paciente=paciente).exists():
                        validacion = 3
                    else:
                        return render(request,"nuevahistoria.html",{"paciente":paciente,"usuario":usuario,"sesion":request.session.get('validar')})
                else:
                    validacion = 2
            return render(request,"historiasclinicas.html",{"usuario":usuario,"pacientes":pacientes,"historiaclinica":historiaclinica,"validacion":validacion,"sesion":request.session.get('validar')})
        else:
            return redirect('/')
   

def verhistoriaclinica(request,id):
    historiaclinica = HistoriasClinica.objects.get(id=idhistoria)
    return render(request,"detallehistoriasclinicas.html",{"historiaclinica":historiaclinica,"sesion":request.session.get('validar')})

def historialregistrar(request,idhistoria):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if usuario.rol == "Administrador" or usuario.rol == "Prestador":
                d2 = 0
                validar = 0
                fecha1 = "2021-12-12"
                fecha2 = "2021-12-12"
                historiaclinica = HistoriasClinica.objects.get(id=idhistoria)
                consultas = Consulta.objects.filter(historiaclinicas=historiaclinica)
                if request.method == "POST":
                    consultaregister = Consulta(
                    historiaclinicas = historiaclinica,
                    fechaconsulta = request.POST.get("fechaconsulta"),
                    fechaalta = request.POST.get("horaconsulta"),
                    diagnostico = request.POST.get("diagnostico"),
                    tratamiento = request.POST.get("tratamiento"),
                    otrosdatos = request.POST.get("otrosdatos"),
                    observaciones = request.POST.get("observaciones")
                    )
                    consultaregister.save()
                    validar = 1
                historiaclinica = HistoriasClinica.objects.get(id=idhistoria)
                consultas = Consulta.objects.filter(historiaclinicas=historiaclinica)
                if consultas.count() > 1:
                    for con in consultas:
                        if d2 == 0:
                            fecha1 = con.fechaconsulta
                            d2 = 1
                        else:
                            fecha2 = con.fechaconsulta
                            if fecha1 > fecha2:
                                fecha1 = fecha1
                            else:
                                fecha1 = fecha2
                    consultas = Consulta.objects.get(fechaconsulta=fecha1, historiaclinicas = historiaclinica)
                else:
                    for con in consultas:
                        consultas = Consulta.objects.get(id=con.id)
                return render(request,"historialregistrar.html",{"usuario":usuario,"paciente":historiaclinica,"consulta":consultas,"validar":validar,"sesion":request.session.get('validar')})
            else:
                return redirect('/dashboard')
        else:
            return redirect('/')

def editarhistoriaclinica(request,idhis):
    d2 = 0
    validar = 0
    registro1consulta = 0
    histori = HistoriasClinica.objects.get(id=idhis)
    registro2consulta = 0
    fecha1 = "2021-12-12"
    fecha1registro2 = "2021-12-12"
    fecha2registro2 = "2021-12-12"
    fecha2 = "2021-12-12"
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if usuario.rol == "Administrador" or usuario.rol == "Prestador":
                historiaclinica = HistoriasClinica.objects.get(id=idhis)
                consultas = Consulta.objects.filter(historiaclinicas=historiaclinica)
                if consultas.count() > 2:
                    for con in consultas:
                        if d2 == 0:
                            fecha1 = con.fechaconsulta
                            d2 = 1
                        else:
                            fecha2 = con.fechaconsulta
                            if fecha1 > fecha2:
                                fecha1 = fecha1
                            else:
                                fecha1 = fecha2
                        if Consulta.objects.filter(id=con.id, fechaconsulta= fecha1).exists():
                            registro1consulta = Consulta.objects.get(id=con.id, fechaconsulta= fecha1)
                    d2 = 0
                    for co in consultas:
                        if Consulta.objects.filter(id=co.id,fechaconsulta=fecha1).exists():
                            idco2 = co.id
                        else:
                            if d2 == 0:
                                fecha1registro2 = co.fechaconsulta
                                d2 = 1
                            else:
                                fecha2registro2 = co.fechaconsulta
                                if fecha1registro2 > fecha2registro2:
                                    fecha1registro2 = fecha1registro2
                                else:
                                    fecha1registro2 = fecha2registro2
                            if  Consulta.objects.filter(id=co.id, fechaconsulta= fecha1registro2).exists():
                                registro2consulta = Consulta.objects.get(id=co.id, fechaconsulta= fecha1registro2)
                    consultas=[]
                    return render(request,'editarhistoria.html',{"usuario":usuario,"edit1":registro1consulta,"edit2":registro2consulta,"consultas":consultas,"paciente":histori,"sesion":request.session.get('validar')})
                else:
                    if request.method == "POST":
                        for editcon in consultas:
                            edithistoria = Consulta.objects.get(id=editcon.id)
                            if request.POST.get("fechaconsultica"+str(editcon.id)):
                                edithistoria.fechaconsulta = request.POST.get("fechaconsultica"+str(editcon.id))
                            
                            edithistoria.fechaalta = request.POST.get("horaconsultica"+str(editcon.id))
                            edithistoria.diagnostico = request.POST.get("diagnosticico"+str(editcon.id))
                            edithistoria.tratamiento = request.POST.get("tratamientico"+str(editcon.id))
                            edithistoria.otrosdatos = request.POST.get("otrosdaticos"+str(editcon.id))
                            edithistoria.observaciones = request.POST.get("observacione"+str(editcon.id))
                            edithistoria.save()
                            validar = 1
                            print("Editado correctamente")
                            consultas = Consulta.objects.filter(historiaclinicas=historiaclinica)
                    return render(request,'editarhistoria.html',{"usuario":usuario,"consultas":consultas,"paciente":histori,"validar":validar,"sesion":request.session.get('validar')})
            else:
                return redirect('/dashboard')
        else:
            return redirect('/')

def edithistori(request,id1,id2):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            validar = 0
            histori = Consulta.objects.get(id=id1)
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if usuario.rol == "Administrador" or usuario.rol == "Prestador":
                if request.method == "POST":
                    edit1consul = Consulta.objects.get(id=id1)
                    edit2consul = Consulta.objects.get(id=id2)
                    if request.POST.get("fechaconsulta1"):
                        edit1consul.fechaconsulta = request.POST.get("fechaconsulta1")
                    if request.POST.get("horaconsulta1"):
                        edit1consul.fechaalta = request.POST.get("horaconsulta1")
                    edit1consul.diagnostico = request.POST.get("diagnostico1")
                    edit1consul.tratamiento = request.POST.get("tratamiento1")
                    edit1consul.otrosdatos = request.POST.get("otrosdatos1")
                    edit1consul.observaciones = request.POST.get("observaciones1")
                    edit1consul.save()
                    if request.POST.get("fechaconsulta2"):
                        edit2consul.fechaconsulta = request.POST.get("fechaconsulta2")
                    if request.POST.get("horaconsulta2"):
                        edit2consul.fechaalta = request.POST.get("horaconsulta2")
                    edit2consul.diagnostico = request.POST.get("diagnostico2")
                    edit2consul.tratamiento = request.POST.get("tratamiento2")
                    edit2consul.otrosdatos = request.POST.get("otrosdatos2")
                    edit2consul.observaciones = request.POST.get("observaciones2")
                    edit2consul.save()
                    edit1consul = Consulta.objects.get(id=id1)
                    edit2consul = Consulta.objects.get(id=id2)
                    print("Todo ok")
                    consultas = []
                    return render(request,'editarhistoria.html',{"usuario":usuario,"edit1":edit1consul,"edit2":edit2consul,"paciente":histori.historiaclinicas,"validar":validar,"sesion":request.session.get('validar')})
            else:
                return redirect('/dashboard')
        else:
            return redirect('/')


def eliminarcita(request,id1citas):
    citadelete = Cita.objects.get(id=id1citas)
    citadelete.delete()
    return redirect('/citas') 

@csrf_exempt
def historialviewpdf(request):
    if request.session.get('validar') == False:
        return redirect('/')
    else: 
        if request.method == 'POST':
            valida = False
            historial = HistoriasClinica.objects.get(id=request.POST.get("selecthistorial"))
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if usuario.rol == "Asistente":
                usuario = Usuario.objects.filter(id=request.session.get('user')).values()
                valida = True
            else:
                usuario=[]
            print(valida)
            paciente = Paciente.objects.filter(id=historial.paciente.id).values()
            consultas = Consulta.objects.filter(historiaclinicas=historial).values()
            return JsonResponse({
                "success": True,
                "valida": valida,
                "historial":list(consultas),
                "paciente":list(paciente),
                "usuari":list(usuario)
            })

def bloquearobservaciones(request,asis):
    asistente = asis.split('-', 1)
    val = 0
    for asi in asistente:
        if val == 1:
            asistent = Usuario.objects.get(usuario=asi)
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if asistent.permisoscomentario == "Si":
                asistent.permisoscomentario = "No"
                usuario.permisoscomentario = "No"
            else:
                asistent.permisoscomentario = "Si"
                usuario.permisoscomentario = "Si"
            asistent.save()
            usuario.save()
        val +=1
    val = 0
    return redirect('/dashboard')

#Cambiar Contraseña 
def cambiocontraseña(request,iduser):
    if request.session.get('validar') == False:
        return redirect('/')
    else:
        if request.session.get('user'):
            validar =  0
            usuario = Usuario.objects.get(id=request.session.get('user'))
            if request.method == "POST":
                usuario = Usuario.objects.get(id=iduser)
                clave = request.POST.get("conantigua")
                base64_message = usuario.clave
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                if clave == message:
                    if request.POST.get("connueva") == request.POST.get("conconfirmar"):
                        clave = request.POST.get("conconfirmar")
                        message_bytes = clave.encode('ascii')
                        base64_bytes = base64.b64encode(message_bytes)
                        base64_message = base64_bytes.decode('ascii')
                        usuario.clave = base64_message
                        usuario.save()
                        validar = 3
                    else:
                        validar = 2
                else:
                    validar = 1
            return render(request,"cambiocontraseña.html",{"usuario":usuario,"validar":validar})
        else:
            return redirect('/')
    
    