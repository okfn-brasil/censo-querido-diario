from django import forms
from django.conf import settings
from django_select2 import forms as s2forms

from .models import Mapeamento


class PostCityForm(forms.ModelForm):
    data_inicial = forms.DateField(label='Qual a data do arquivo mais antigo disponível online?',
                                    help_text='O município publica diários oficiais na internet desde quando? Informe a data do primeiro diário oficial cujo arquivo é possível visualizar na página que irá cadastrar neste formulário.',
                                   input_formats=settings.DATE_INPUT_FORMATS,
                                   widget=forms.DateInput(attrs={
                                   'placeholder':'DD/MM/AAAA',
                                    'onkeyup':"this.value=this.value.replace(/^(\d\d)(\d)$/g,'$1/$2').replace(/^(\d\d\/\d\d)(\d+)$/g,'$1/$2').replace(/[^\d\/]/g,'')"
                                   }),
                                   required=False)

    class Meta:
        model = Mapeamento
        fields = ('municipio', 'is_online','data_inicial', 'tipo_arquivo', 'fonte_1', 'fonte_2', 'fonte_3',
                  'fonte_4',)
        widgets = {'municipio': s2forms.Select2Widget}
        labels = {
            'municipio': 'Selecione o município',
            'fonte_1': 'Informe uma fonte de publicação de arquivos',
            'fonte_2': 'Informe uma fonte de publicação de arquivos',
            'fonte_3': 'Informe uma fonte de publicação de arquivos',
            'fonte_4': 'Informe uma fonte de publicação de arquivos',
            'is_online': 'Existe uma fonte de publicação disponível online?',
            'tipo_arquivo': 'Qual o formato dos arquivos?',
        }
        help_texts = {
            'municipio': 'Digite o nome do município que deseja cadastrar. Se ele não constar na lista disponível, significa que seu mapeamento já foi realizado. Saiba mais <a href="/sobre/#faq-1">aqui</a>.',
            'is_online': 'É possível encontrar o diário oficial do município publicado em alguma página da internet? Caso não seja possível, clique <a href="sobre/#faq-5">aqui</a> para saber mais.',            
            'fonte_1': 'URL do portal público principal que disponibiliza o diário oficial deste município.'
        }