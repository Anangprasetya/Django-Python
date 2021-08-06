from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.models import Komik
from apps.forms import KomikForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url=settings.LOGIN_URL)
def signup(request):
	if request.POST:
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "User berhasil dibuat !")
			return redirect('signup')
		else:
			messages.error(request, "Terjadi kesalahan !")
			return redirect('signup')
	else:
		form = UserCreationForm()
		data = {
			'form': UserCreationForm(),

		}

		return render(request, 'signup.html', data)


@login_required(login_url=settings.LOGIN_URL)
def hapus_komik(request, id_komik):
	komik = Komik.objects.filter(id=id_komik)
	komik.delete()
	messages.success(request, "Data berhasil dihapus")
	return redirect('komik')


@login_required(login_url=settings.LOGIN_URL)
def ubah_komik(request, id_komik):
	komik = Komik.objects.get(id = id_komik)
	if request.POST:
		form = KomikForm(request.POST, request.FILES, instance = komik)
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


@login_required(login_url=settings.LOGIN_URL)
def komik(request):
	ambilKomik = Komik.objects.all()
	# filter dan join, limit
	
	# ambilKomik = Komik.objects.filter(id_negara__nama = 'Jepang')[:2]
	data = {
		'judul' : 'Komik | Anang',
		'komik' : ambilKomik,
	}
	return render(request, 'komik.html', data)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
	data = {
		'judul' : 'Penerbit'
	}
	return render(request, 'penerbit.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambah_komik(request):
	if request.POST:
		form = KomikForm(request.POST, request.FILES)
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


