from rest_framework import serializers
from .models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = ['id', 'titulo', 'descripcion', 'fecha_inicio', 'investigador', 'empresa']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.investigador:
            rep['investigador'] = instance.investigador.username
        else:
            rep['investigador'] = None

        if instance.empresa:
            rep['empresa'] = instance.empresa.nombre
        else:
            rep['empresa'] = None

        return rep