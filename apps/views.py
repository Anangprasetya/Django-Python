from django.shortcuts import render
from django.http import HttpResponse
from apps.models import Komik
from apps.forms import KomikForm


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


def tambah_komik(request):
	form = KomikForm();
	data = {
		'judul' : 'Tambah Data Komik',
		'form' : form,
	}

	return render(request, 'tambah-buku.html', data)


