from .models import CorreoAutorizado

def es_correo_valido(correo):
    return CorreoAutorizado.objects.filter(email=correo.lower()).exists()