from django.shortcuts import render
from django.http import HttpResponse


def komik(request):
    judul = "Belajar Django"
    komik = ["mereka", "dia", "akan", "segera"]
    data = {
        'judul' : judul,
        'penulis' : 'Anang Nur Prasetya',
        'komik' : komik,
    }
    return render(request, 'komik.html', data)

def penerbit(request):
    return HttpResponse('Ini adalah halaman penerbit')


