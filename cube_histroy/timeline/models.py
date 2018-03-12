from django.db import models

class Evento(models.Model):
	idEvento = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=5000)
	fecha = models.DateField('fecha')
	CONTINENTES_CHOICES = (
		(1, 'America'),
		(2, 'Africa'),
		(3, 'Asia'),
		(4, 'Europa'),
		(5, 'Oceania'),
	)
	continente = models.IntegerField(choices=CONTINENTES_CHOICES, default=1)
	def __str__(self):
		return self.titulo
	def descripcionEvento(self):
		return self.descripcion
	def fechaEvento(self):
		return self.fecha
	def continenteEvento(self):
		return self.continente

class Imagen(models.Model):
	idImagen = models.AutoField(primary_key=True)
	fkEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	link = models.CharField(max_length=5000)
	def __str__(self):
		return self.nombre
	def linkImagen(self):
		return self.link

class Fuente(models.Model):
	idFuente = models.AutoField(primary_key=True)
	fkEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=5000)
	link = models.CharField(max_length=5000)
	año = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
	def __str__(self):
		return self.titulo
	def autorFuente(self):
		return self.autor
	def linkFuente(self):
		return self.link
	def anioFuente(self):
		return self.anio