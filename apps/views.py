from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.models import Komik
from apps.forms import KomikForm
from django.contrib import messages


def hapus_komik(request, id_komik):
	komik = Komik.objects.filter(id=id_komik)
	komik.delete()
	messages.success(request, "Data berhasil dihapus")
	return redirect('komik')


def ubah_komik(request, id_komik):
	komik = Komik.objects.get(id = id_komik)
	if request.POST:
		form = KomikForm(request.POST, instance = komik)
		if form.is_valid():
			form.save()
			messages.success(request, "Data Berhasil Di Perbarui")
			return redirect('ubah_komik', id_komik = id_komik)
	else:
		form = KomikForm(instance = komik)
		data = {
			'judul' : 'Ubah Data Komik',
			'form' : form,
			'komik' : komik
		}

		return render(request, 'ubah_komik.html', data)



def komik(request):
	ambilKomik = Komik.objects.all()
	# filter dan join, limit
	
	# ambilKomik = Komik.objects.filter(id_negara__nama = 'Jepang')[:2]
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
	if request.POST:
		form = KomikForm(request.POST)
		if form.is_valid():
			form.save()
			form = KomikForm()
			data = {
				'judul' : 'Tambah Data Komik',
				'form' : form,
				'pesan' : "Data Berhasil Disimpan",
			}
	else:
		form = KomikForm();
		data = {
			'judul' : 'Tambah Data Komik',
			'form' : form,
		}

	return render(request, 'tambah-buku.html', data)


