from django.db import models

class Cita(models.Model):
    fecha = models.DateTimeField()
    paciente = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.paciente} - {self.fecha}"