from django.contrib import admin
from timeline.models import Evento
from timeline.models import Imagen
from timeline.models import Fuente

#admin.site.register(Evento)
#admin.site.register(Imagen)
#admin.site.register(Fuente)

class ImagenInline(admin.StackedInline):
	model = Imagen
	extra = 1

class FuenteInline(admin.StackedInline):
	model = Fuente
	extra = 1

class EventoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['titulo']}),
		('Descripción', {'fields':['descripcion'], 'classes': ['collapse']}),
		('Fecha:', {'fields':['fecha']}),
		('Continente:', {'fields':['continente']}),
	]
	inlines = [ImagenInline, FuenteInline]

admin.site.register(Evento, EventoAdmin)