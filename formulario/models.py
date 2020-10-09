from django.db import models

class Municipio(models.Model):
    ibge = models.IntegerField() 
    ibge7 = models.IntegerField()
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=128)
    regiao = models.CharField(max_length=15)
    populacao_2010 = models.IntegerField(null=True)
    capital = models.BooleanField(default=False)

    def __str__(self):
        return '%s (%s)' % (self.municipio, self.uf)


class Mapeamento(models.Model):
    IS_ONLINE = (
        (1, 'Sim'),
        (2, 'Não'),
        (3, 'Sem confirmação'),
        )

    TIPOS_ARQUIVOS = (
        (1, 'PDF texto'),
        (2, 'PDF imagem'),
        (3, 'DOCX'),
        (4, 'HTML'),
        (5, 'TXT'),
        (6, 'Outro formato'),
        )

    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    fonte_1 = models.URLField(blank=True, null=True)
    fonte_2 = models.URLField(blank=True, null=True)
    fonte_3 = models.URLField(blank=True, null=True)
    fonte_4 = models.URLField(blank=True, null=True)
    is_online = models.IntegerField(choices=IS_ONLINE, default=3)
    data_inicial = models.DateField(blank=True, null=True)
    tipo_arquivo = models.IntegerField(choices=TIPOS_ARQUIVOS, blank=True, null=True)
    validacao = models.BooleanField(default=False)
    navegacao = models.FloatField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    tem_anomalia = models.BooleanField(default=False)
    anomalia_obs = models.TextField(blank=True, null=True)


    def __str__(self):
        return '%s' % (self.municipio)