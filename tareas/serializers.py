from rest_framework import serializers
from tareas.models import Tareas

class TareaSerializer(serializers.ModelSerializer):
    usuario_asignado = serializers.StringRelatedField()
    class Meta:
        model = Tareas
        fields = '__all__'
        depth = 1