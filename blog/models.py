from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
