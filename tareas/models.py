from django.db import models
from django.contrib.auth.models import User

class Tareas(models.Model):

    ESTADOS = [
        ('BACKLOG', 'Backlog'),
        ('TO DO', 'To Do'),
        ('DOING', 'Doing'),
        ('TEST', 'Test'),
        ('DONE', 'Done'),
    ]
    
    PRIORIDAD = [
        ('ALTO', 'Alto'),
        ('MEDIO', 'Medio'),
        ('BAJA', 'Baja'),
    ]
    
    nombre = models.CharField(max_length=255, db_index=True)
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='BACKLOG', db_index=True)
    prioridad = models.CharField(max_length=6, choices=PRIORIDAD, default='MEDIO', db_index=True)
    fecha_entrega = models.DateField(db_index=True)
    comentario = models.TextField(blank=True, null=True)
    usuario_asignado = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        related_name='tareas_asignadas',
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.nombre} - {self.estado} - {self.usuario_asignado.username}"
    
    class Meta:
        verbose_name_plural = "Tareas"
        ordering = ['fecha_entrega']  # Orden por defecto para optimizar consultas
