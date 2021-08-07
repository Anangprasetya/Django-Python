from import_export import resources
from .models import Komik

class KomikResource(resources.ModelResource):
    class Meta:
        model = Komik