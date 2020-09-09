from django import forms
from django.conf import settings
from django_select2 import forms as s2forms

from .models import Municipio, Mapeamento


class PostCityForm(forms.ModelForm):
    data_inicial = forms.DateField(label='Desde quando o minicípio publica os diários oficiais de forma online?',
                                   input_formats=settings.DATE_INPUT_FORMATS,
                                   widget=forms.DateInput(attrs={'placeholder':'DD/MM/YYYY'}),
                                   required=False)

    class Meta:
        model = Mapeamento
        fields = ('municipio', 'is_online', 'link_do', 'data_inicial', 'tipo_arquivo')
        widgets = {'municipio': s2forms.Select2Widget}
        labels = {
            'municipio': 'Selecione o Município',
            'link_do': 'Informe as fontes de publicação',
            'is_online': 'Existe uma fonte de publicação disponível de forma online?',
            'tipo_arquivo': 'Qual o formato dos arquivos?',
        }