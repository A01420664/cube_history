from django.shortcuts import render
from timeline.models import Evento

def index(request):
	my_dic = {'insert_me:"Index"'}
	america = Evento.objects.filter(continente = 1).order_by('fecha')
	africa = Evento.objects.filter(continente = 2).order_by('fecha')
	asia = Evento.objects.filter(continente = 3).order_by('fecha')
	europa = Evento.objects.filter(continente = 4).order_by('fecha')
	oceania = Evento.objects.filter(continente = 5).order_by('fecha')
	my_dic = {'eventos_america':america, 'eventos_africa':africa, 'eventos_asia':asia, 'eventos_europa':europa, 'eventos_oceania':oceania}
	return render(request, 'timeline/index3.html', context=my_dic)