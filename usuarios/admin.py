from django.contrib import admin
from .models import Usuario, CorreoAutorizado
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario, UserAdmin)
admin.site.register(CorreoAutorizado)