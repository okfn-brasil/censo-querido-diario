from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

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
        form.fields['municipio'].queryset = Municipio.objects.filter(mapeamento__isnull=True).order_by('municipio')

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
        cities = Municipio.objects.filter(mapeamento__validacao=True).values(*values_list).order_by('municipio').distinct()
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