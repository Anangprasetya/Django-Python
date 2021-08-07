from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from apps import views
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('komik/', views.komik, name = 'komik'),
    path('penerbit/', views.penerbit),
    path('tambah-komik/', views.tambah_komik, name = 'tambah_komik'),
    path('komik/ubah/<int:id_komik>', views.ubah_komik, name = 'ubah_komik'),
    path('komik/hapus/<int:id_komik>', views.hapus_komik, name='hapus_komik'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', views.signup, name='signup'),
    path('export/', views.export_xls, name='export_xls'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
