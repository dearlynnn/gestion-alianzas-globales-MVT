from rest_framework import serializers
from .models import Empresa, Convenio

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ConvenioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Convenio
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.firmado_por:
            rep[''] = instance.firmado_por.username
        else:
            rep['firmado_por'] = None

        if instance.empresa:
            rep['empresa'] = instance.empresa.nombre
        else:
            rep['empresa'] = None

        return rep
