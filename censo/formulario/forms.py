from django import forms
from django_select2 import forms as s2forms

from .models import Municipio, Mapeamento


class MunicipioWidget(s2forms.ModelSelect2MultipleWidget):
	search_fields = ['municipio__icontains']

class PostCityForm(forms.ModelForm):
	class Meta:
		model = Mapeamento
		fields = ('municipio', 'link_do', 'status', 'data_inicial', 'tipo_arquivo')
		widgets = {'municipio': s2forms.Select2Widget}