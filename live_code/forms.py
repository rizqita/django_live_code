from django import forms
from .models import Barang

class inputBarang(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ('nama','gambar','harga','detail')
