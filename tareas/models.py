from django.db import models

class Tarea(models.Model):
    # Opciones para el campo 'estado'
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]
    
    # Campo: título (texto corto, obligatorio)
    titulo = models.CharField(max_length=200)
    
    # Campo: descripción (texto largo, opcional)
    descripcion = models.TextField(blank=True, null=True)
    
    # Campo: estado (con opciones predefinidas)
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS, 
        default='pendiente'
    )
    
    # Campo: fecha creación (automática)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo