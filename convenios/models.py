from django.db import models
from usuarios.models import Usuario  # o como se llame tu modelo personalizado

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    nit = models.CharField(max_length=50, unique=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    correo_contacto = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

class Convenio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    firmado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    documento_pdf = models.FileField(upload_to='convenios/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} – {self.empresa.nombre}"
