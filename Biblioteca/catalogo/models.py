from django.db import models

# Create your models here.
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField()

    def __str__(self):
        return f"{self.id_autor} - {self.nombre} - {self.apellido}"
    
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=20)
    num_pag = models.IntegerField()
    editorial = models.CharField(max_length=100)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    
