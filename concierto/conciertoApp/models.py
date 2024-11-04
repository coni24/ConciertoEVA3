from django.db import models

class Persona(models.Model):
    RUT = models.CharField(max_length=9, unique=True)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Telefono = models.CharField(max_length=9)
    Edad = models.IntegerField()
    Correo = models.EmailField()

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

class Concierto(models.Model):
    Fecha = models.DateField()
    Hora = models.TimeField(default="00:00")
    Lugar = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=15)
    Capacidad = models.IntegerField()

    def __str__(self):
        return f"{self.Lugar}"
    
class Entrada(models.Model):
    Categoria = models.CharField(max_length=20)
    Descripcion = models.TextField()
    NumeroAsiento = models.IntegerField(default=1)
    Precio = models.IntegerField()
    Sector = models.CharField(max_length=20)
    Concierto = models.ForeignKey(Concierto, on_delete=models.CASCADE, related_name="entradas")
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="entradas",null=True, blank=True)

    def __str__(self):
        return f"Entrada {self.NumeroAsiento} - {self.Categoria}"
    