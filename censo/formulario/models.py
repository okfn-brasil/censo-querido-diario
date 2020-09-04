from django.db import models

class Municipio(models.Model):
	ibge = models.IntegerField() 
	ibge7 = models.IntegerField()
	uf = models.CharField(max_length=2)
	municipio = models.CharField(max_length=128)
	regiao = models.CharField(max_length=15)
	populacao_2010 = models.IntegerField()
	capital = models.BooleanField()

class Mapeamento(models.Model):
	STATUS = (
		(1, 'Público'),
		(2, 'Não público'),
		(3, 'Sem informação'),
		)

	TIPOS_ARQUIVOS = (
		(1, 'PDF'),
		(2, 'Docx'),
		)

	municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)
	status = models.IntegerField(choices=STATUS)
	data_inicial = models.DateField()
	link_do = models.URLField()
	tipo_arquivo = models.IntegerField(choices=TIPOS_ARQUIVOS)
	validacao = models.BooleanField()
	navegacao = models.FloatField()
