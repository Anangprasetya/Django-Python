from django.forms import ModelForm
from apps.models import Komik


class KomikForm(ModelForm):
    class Meta:
        model = Komik
        fields = '__all__'
        # exclude = [''] kecuali 
    