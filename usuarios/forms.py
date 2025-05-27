from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .utils import es_correo_valido

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email').lower() 
        
        if not es_correo_valido(email):
            raise forms.ValidationError("Este correo no está autorizado por RNI o Talento Humano.")
        
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con este correo.")

        return email

class AutenticacionForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
