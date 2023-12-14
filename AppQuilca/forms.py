from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from AppQuilca.models import Avatar, Comments


class BusquedaRaquetaForm(forms.Form):
    raqueta = forms.CharField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("raqueta", "usuario", "comentario")
