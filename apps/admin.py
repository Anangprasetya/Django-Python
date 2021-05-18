from django.contrib import admin
from apps.models import *

class KomikAdmin(admin.ModelAdmin):
	list_display = ('judul', 'penulis', 'id_negara', 'jumlah')
	list_filter = ['id_negara']
	search_fields = ['judul', 'penulis'] 
	list_per_page = 2

admin.site.register(Komik, KomikAdmin)
admin.site.register(Negara)

# Register your models here.
