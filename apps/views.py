from django.shortcuts import render
from django.http import HttpResponse


def komik(request):
    return render(request, 'komik.html')

def penerbit(request):
    return HttpResponse('Ini adalah halaman penerbit')


