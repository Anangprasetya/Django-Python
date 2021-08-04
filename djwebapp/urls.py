from django.contrib import admin
from django.urls import path
from apps.views import *
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('komik/', komik, name = 'komik'),
    path('penerbit/', penerbit),
    path('tambah-komik/', tambah_komik, name = 'tambah_komik'),
    path('komik/ubah/<int:id_komik>', ubah_komik, name = 'ubah_komik'),
    path('komik/hapus/<int:id_komik>', hapus_komik, name='hapus_komik'),
    path('masuk/', LoginView.as_view(), name='masuk'),
]
