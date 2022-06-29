"""proyecto_coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_coder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home , name="home"),
    #path('', views.inicio),
    path('cursos', views.cursos, name="cursos"),
    #path('alta_curso/<nombre>', views.alta_curso),
    path('alta_curso', views.curso_formulario),
    path('Alumnos', views.alumnos, name="alumnos"),
    #path('alta_alumno/<nombre>/<apellido>', views.alta_alumno),
    path('alta_alumno', views.alumno_formulario),
    path('Profesores', views.profesores, name='profesores'),
    #path('alta_profesor/<nombre>/<apellido>/<profesion>', views.alta_profesor),
    path('alta_profesor', views.profesor_formulario),
    path('buscar_curso', views.buscar_curso, name="buscar"),
    path('buscar', views.buscar),
    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('elimina_curso/<int:id>' , views.elimina_curso , name="elimina_curso"),
    path('elimina_alumno/<int:id>' , views.elimina_alumno , name="elimina_alumno"),
    path('elimina_profesor/<int:id>' , views.elimina_profesor , name="elimina_profesor"),
    path('editar_curso/<int:id>' , views.editar_c , name="editar_curso" ),
    path('editar_curso/' , views.editar_c , name="editar_curso"),
    path('editar_profesor/<int:id>' , views.editar_p , name="editar_profesor" ),
    path('editar_profesor/' , views.editar_p , name="editar_profesor"),
    path('editar_alumno/<int:id>' , views.editar_a , name="editar_alumno" ),
    path('editar_alumno/' , views.editar_a , name="editar_alumno"),
    path('editarPerfil', views.editarPerfil , name="EditarPerfil"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)