from django.shortcuts import render
from django.http import HttpResponse
from apps.models import Komik


def komik(request):
	ambilKomik = Komik.objects.all()
	data = {
		'judul' : 'Komik | Anang',
		'komik' : ambilKomik,
	}
	return render(request, 'komik.html', data)

def penerbit(request):
	data = {
		'judul' : 'Penerbit'
	}
	return render(request, 'penerbit.html', data)


