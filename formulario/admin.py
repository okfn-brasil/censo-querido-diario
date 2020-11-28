from django.contrib import admin

from formulario.models import Municipio, Mapeamento


class MunicipioAdmin(admin.ModelAdmin):
    fields = ('ibge', 'ibge7', 'municipio', 'uf', 'regiao', 'populacao_2020', 'capital')
    readonly_fields = ('ibge', 'ibge7', 'municipio', 'uf', 'regiao', 'populacao_2020', 'capital')

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super(MunicipioAdmin, self).get_queryset(request)
        return qs.order_by('municipio')

class MapeamentoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MapeamentoAdmin, self).get_queryset(request)
        return qs.filter(validacao=False)

class MapeamentoCemMilhabitante(Mapeamento):
    class Meta:
        proxy = True

class MapeamentoCemMilhabitanteAdmin(MapeamentoAdmin):
    def get_queryset(self, request):
        qs = super(MapeamentoAdmin, self).get_queryset(request)
        return qs.filter(municipio__populacao_2020__gt=100000, validacao=False)

class MapeamentoValidado(Mapeamento):
    class Meta:
        proxy = True

class MapeamentoValidadoAdmin(MapeamentoAdmin):
    def get_queryset(self, request):
        qs = super(MapeamentoAdmin, self).get_queryset(request)
        return qs.filter(validacao=True)

class MapeamentoValidadoCemMilHabitante(Mapeamento):
    class Meta:
        proxy = True

class MapeamentoValidadoCemMilHabitanteAdmin(MapeamentoAdmin):
    def get_queryset(self, request):
        qs = super(MapeamentoAdmin, self).get_queryset(request)
        return qs.filter(municipio__populacao_2020__gt=100000, validacao=True)

class MapeamentoValidadoCapitai(Mapeamento):
    class Meta:
        proxy = True

class MapeamentoValidadoCapitaiAdmin(MapeamentoAdmin):
    def get_queryset(self, request):
        qs = super(MapeamentoAdmin, self).get_queryset(request)
        return qs.filter(municipio__capital=True, validacao=True)


admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Mapeamento, MapeamentoAdmin)
admin.site.register(MapeamentoCemMilhabitante, MapeamentoCemMilhabitanteAdmin)
admin.site.register(MapeamentoValidado, MapeamentoValidadoAdmin)
admin.site.register(MapeamentoValidadoCemMilHabitante, MapeamentoValidadoCemMilHabitanteAdmin)
admin.site.register(MapeamentoValidadoCapitai, MapeamentoValidadoCapitaiAdmin)
