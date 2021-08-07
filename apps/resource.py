from import_export import resources
from import_export.fields import Field
from apps.models import Komik

class KomikResource(resources.ModelResource):
    id_negara__nama = Field(attribute='id_negara', column_name='negara')
    class Meta:
        model = Komik
        fields = ['judul', 'tanggal', 'id_negara__nama', 'penerbit', 'jumlah']
        export_order = ['judul', 'id_negara__nama', 'penerbit', 'jumlah', 'tanggal']
