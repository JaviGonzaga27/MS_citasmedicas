from rest_framework import serializers
from citas_app.models import Cita

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'fecha', 'paciente', 'doctor']