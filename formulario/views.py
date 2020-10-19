from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.http import HttpResponse
import csv
# import icu


from .forms import PostCityForm
from .models import Municipio, Mapeamento


REGIONS = {
    'norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'centro-oeste': ['DF', 'GO', 'MT', 'MS'],
    'sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'sul': ['PR', 'RS', 'SC'],
}


def post_city(request):
    if request.method == 'POST':
        form = PostCityForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        return render(request, 'error_template.html', {'form': form})
    else:
        form = PostCityForm()
        form.fields['municipio'].queryset = Municipio.objects.filter(
            mapeamento__isnull=True).order_by('municipio')

    return render(request, 'form.html', {'form': form})


def mapped_cities(request):
    page = request.GET.get('page', 1)
    state = request.GET.get('state')
    region = request.GET.get('region')
    values_list = [
        'municipio',
        'uf',
        'mapeamento__fonte_1',
        'mapeamento__fonte_2',
        'mapeamento__fonte_3',
        'mapeamento__fonte_4'
    ]
    if state:
        state = state.upper()
        cities = Municipio.objects.filter(mapeamento__validacao=True, uf=state).values(*values_list).order_by('municipio').distinct()
        total_cities = Municipio.objects.filter(uf=state).count()
        context = state
    elif region:
        cities = Municipio.objects.filter(mapeamento__validacao=True, uf__in=REGIONS[region]).values(*values_list).order_by('municipio').distinct()
        total_cities = Municipio.objects.filter(uf__in=REGIONS[region]).count()
        context = region
    else:
        cities = Municipio.objects.filter(mapeamento__validacao=True).values(
            *values_list).order_by('municipio').distinct()
        total_cities = Municipio.objects.count()
        context = 'Brasil'

    percentage = round(len(cities)/total_cities*100, 2)

    # Pagination on interface
    paginator = Paginator(cities, 50)

    try:
        cities_page = paginator.page(page)
    except PageNotAnInteger:
        cities_page = paginator.page(1)
    except EmptyPage:
        cities_page = paginator.page(paginator.num_pages)

    return render(request, 'mapped_cities.html', {'cities': cities_page, 'percentage': percentage, 'context': context})


def about(request):
    return render(request, 'sobre.html')

def faq(request):
    return render(request, 'faq.html')


def download_csv_data(request):

    chk_cidades_sem_map = request.POST.get('chk_cidades_sem_map')

    # response content type
    response = HttpResponse(content_type='text/csv')

    # decide the file name
    response['Content-Disposition'] = 'attachment; filename="base_mapeamento.csv"'

    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    lista = []

    # get data from database
    mapeados = Mapeamento.objects.all().order_by('municipio')

    for municipio in mapeados:
        lista.append([
            smart_str(municipio.municipio),
            smart_str(municipio.municipio.ibge),
            smart_str(municipio.municipio.ibge7),
            smart_str(municipio.municipio.uf),
            smart_str(municipio.municipio.regiao),
            smart_str(municipio.municipio.populacao_2010),
            smart_str(municipio.municipio.capital),
            smart_str(municipio.fonte_1),
            smart_str(municipio.fonte_2),
            smart_str(municipio.fonte_3),
            smart_str(municipio.fonte_4),
            smart_str(municipio.is_online),
            smart_str(municipio.data_inicial),
            smart_str(municipio.get_tipo_arquivo_display()),
            smart_str(municipio.validacao),
            smart_str(municipio.navegacao),
            smart_str(municipio.observacoes),
        ])

    # if chk is true, gets all municipios from Municipio table, excluding those that are in Mapeamento table
    if chk_cidades_sem_map:
        nao_mapeados = Municipio.objects.exclude(id__in=mapeados).order_by('municipio')
        for municipio in nao_mapeados:
            lista.append([ smart_str(municipio.municipio) ])

    # sorted by Municipio 
    # collator = icu.Collator.createInstance(icu.Locale('pt_BR.UTF-8'))
    # sorted_lista = sorted(lista, key=lambda row: collator.getSortKey(row[0]))
    sorted_lista = sorted(lista)

    # write the headers
    sorted_lista.insert(0, [
        smart_str(u"municipio"),
        smart_str(u"IBGE"),
        smart_str(u"IBGE7"),
        smart_str(u"UF"),
        smart_str(u"regiao"),
        smart_str(u"populacao_2010"),
        smart_str(u"eh_capital"),
        smart_str(u"fonte_1"),
        smart_str(u"fonte_2"),
        smart_str(u"fonte_3"),
        smart_str(u"fonte_4"),
        smart_str(u"is_online"),
        smart_str(u"data_inicial"),
        smart_str(u"tipo_arquivo"),
        smart_str(u"validacao"),
        smart_str(u"navegacao"),
        smart_str(u"observacoes"),
    ])

    writer.writerows(sorted_lista)

    return response
