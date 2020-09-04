from django import forms

from .models import Mapeamento

class PostCityForm(forms.ModelForm):
	class Meta:
		model = Mapeamento
		fields = ('municipio', 'link_do', 'status', 'data_inicial', 'tipo_arquivo')