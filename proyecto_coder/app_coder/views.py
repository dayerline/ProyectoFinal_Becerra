from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso, Alumno, Profesor, Avatar
from django.template import loader
from app_coder.forms import Curso_Formulario, Alumno_Formulario, Profesor_Formulario, UserEditForm
from  django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, "padre.html")

def home(request):
    return render(request, "home.html")

@login_required
def cursos(request):
    cursos= Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento= plantilla.render(dicc)
    return HttpResponse( documento)


def alumnos(request):
    alumnos= Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumno.html")
    documento= plantilla.render(dicc)
    return HttpResponse( documento)


def profesores(request):
    profesores= Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla= loader.get_template("profesor.html")
    documento= plantilla.render(dicc)
    return HttpResponse ( documento)


def alta_curso(request, nombre):
    curso= Curso(nombre= nombre, camada=23454)
    curso.save()
    texto=f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse ( texto )


def curso_formulario(request):

    if request.method =="POST":

        mi_formulario = Curso_Formulario( request.POST )
        if mi_formulario.is_valid():
            datos=(mi_formulario.cleaned_data)
        
        curso= Curso( nombre=datos['nombre'] , camada=datos['camada'])
        curso.save()
        
        return render( request , "curso_formulario.html")

    return render( request, "curso_formulario.html")


def alumno_formulario(request):

    if request.method =="POST":

        mi_formulario = Alumno_Formulario( request.POST )
        if mi_formulario.is_valid():
            datos=(mi_formulario.cleaned_data)

        alumno= Alumno( nombre=datos['nombre'] , apellido=datos['apellido'])
        alumno.save()
        return render( request, "alumno_formulario.html")

    return render( request, "alumno_formulario.html")


def profesor_formulario(request):

    if request.method =="POST":
        mi_formulario= Profesor_Formulario( request.POST)
        if mi_formulario.is_valid():
            datos=(mi_formulario.cleaned_data)

        profesor= Profesor( nombre=datos['nombre'] , apellido=datos['apellido'] , profesion=datos['profesion'])
        profesor.save()
        return render( request, "profesor_formulario.html")

    return render( request, "profesor_formulario.html")


def buscar_curso(request):
    return render( request, "buscar_curso.html")


def buscar(request):
    if request.GET['nombre']:
        nombre= request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})


def login_request(request):
    
    if request.method =="POST":
        form = AuthenticationForm( request, data= request.POST)

        if form.is_valid():
            usuario= form.cleaned_data.get("username")
            contraseña= form.cleaned_data.get("password")
            user= authenticate(username=usuario , password=contraseña)

            if user is not None:
                login(request, user)
                avatares= Avatar.objects.filter(user=request.user.id)
                return render( request, "inicio.html", {"url":avatares[0].imagen.url} )
            else:
                return HttpResponse("Usuario Incorrecto")

        else:
            return HttpResponse(f"Form Incorrecto {form}")
    
    form= AuthenticationForm()
    return render( request, "login.html", {"form":form})


def register(request):
    
    if request.method =='POST':
        
        form= UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render( request,"register.html", {"form":form})


def elimina_curso( request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso= Curso.objects.all()
    return render( request, "cursos.html" , {"cursos": curso})


def elimina_alumno( request , id ):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno= Alumno.objects.all()
    return render( request, "alumno.html" , {"alumno": alumno})


def elimina_profesor( request , id ):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesor= Profesor.objects.all()
    return render( request, "profesor.html" , {"profesor": profesor})


def editar_c(request , id):
    curso= Curso.objects.get(id=id)

    if request.method == "POST":
        mi_formu = Curso_Formulario(request.POST)

        if mi_formu.is_valid():
            datos= (mi_formu.cleaned_data)
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso= Curso.objects.all()
            return render(request , "cursos.html", {"cursos": curso})
    else:
        mi_formu= Curso_Formulario(initial={'nombre':curso.nombre, "camada":curso.camada})
    return render( request, "editar_curso.html", {'mi_formu':mi_formu , "curso":curso})


def editar_p(request , id):
    profesor= Profesor.objects.get(id=id)

    if request.method == "POST":
        mi_form = Profesor_Formulario(request.POST)

        if mi_form.is_valid():
            datos= (mi_form.cleaned_data)
            profesor.nombre = datos['nombre']
            profesor.apellido = datos['apellido']
            profesor.profesion = datos['profesion']
            profesor.save()

            profesores= Profesor.objects.all()
            return render(request , "profesor.html", {"profesores": profesores})
            
    else:
        mi_form= Profesor_Formulario(initial={'nombre':profesor.nombre, "apellido":profesor.apellido, "profesion":profesor.profesion})
    return render( request, "editar_profesor.html", {'mi_form':mi_form , "profesor":profesor})


def editar_a(request , id):
    alumno= Alumno.objects.get(id=id)

    if request.method == "POST":
        mi_forms = Alumno_Formulario(request.POST)

        if mi_forms.is_valid():
            datos= (mi_forms.cleaned_data)
            alumno.nombre = datos['nombre']
            alumno.apellido = datos['apellido']
            alumno.save()

            alumnos= Alumno.objects.all()
            return render(request , "alumno.html", {"alumnos": alumnos})
            
    else:
        mi_forms= Alumno_Formulario(initial={'nombre':alumno.nombre, "apellido":alumno.apellido})
    return render( request, "editar_alumno.html", {'mi_forms':mi_forms , "alumno":alumno})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})



#def alta_profesor(request, nombre, apellido, profesion):
    #profesor= Profesor(nombre= nombre, apellido= apellido, profesion= profesion)
    #profesor.save()
    #texto= f"Se guardo en la BD el Profesor: {profesor.nombre} Apellido: {profesor.apellido} Profesion: {profesor.profesion}"
    #return HttpResponse (texto)

#def alta_alumno(request, nombre, apellido):
    #alumno= Alumno(nombre= nombre, apellido= apellido)
    #alumno.save()
    #texto= f"Se guardo en la BD el Alumno: {alumno.nombre} Apellido {alumno.apellido}"
    #return HttpResponse ( texto )