from django.shortcuts import render
from django.http import HttpResponse


def komik(request):
	return HttpResponse('Ini adalah halaman Komik')

def penerbit(request):
    return HttpResponse('Ini adalah halaman penerbit')


