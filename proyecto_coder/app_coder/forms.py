from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Curso_Formulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    camada= forms.IntegerField()


class Alumno_Formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)


class Profesor_Formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    profesion= forms.CharField(max_length=30)

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="modificar")
    password1: forms.Field(label="contraseña" , widget=forms.PasswordInput)
    password2: forms.Field(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}
