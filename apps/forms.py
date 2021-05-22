from django.forms import ModelForm
from django import forms
from apps.models import Komik


class KomikForm(ModelForm):
    class Meta:
        model = Komik
        fields = '__all__'
        # exclude = [''] kecuali 

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'id_negara' : forms.Select({'class':'form-control'}),
        }


    