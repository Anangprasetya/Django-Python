from django.db import models

# Create your models here.

class Negara(models.Model):
	nama = models.CharField(max_length=50)
	keterangan = models.TextField()

	def __str__(self):
		return self.nama

class Komik(models.Model):
	judul = models.CharField(max_length=50)
	penulis = models.CharField(max_length=40)
	penerbit = models.CharField(max_length=40)
	jumlah = models.IntegerField(null=True)
	id_negara = models.ForeignKey(Negara, on_delete = models.CASCADE, null=True)

	def __str__(self):
		return self.judul
