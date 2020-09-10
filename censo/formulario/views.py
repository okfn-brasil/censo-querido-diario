from django.shortcuts import render

from .forms import PostCityForm
from .models import Municipio, Mapeamento


def post_city(request):
    if request.method == 'POST':
        form = PostCityForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base.html')
        return render(request, 'error_template.html', {'form': form})
    else:
        form = PostCityForm()
        form.fields['municipio'].queryset = Municipio.objects.filter(validacao=False).order_by('municipio')

    return render(request, 'form.html', {'form': form})


def validated_cities(request):
    cities = Municipio.objects.filter(validacao=True).values('municipio', 'uf', 'mapeamento__links_fontes__link').distinct()
    total_cities = Municipio.objects.count()
    percentage = round(len(cities)/total_cities*100, 2)

    return render(request, 'validated_cities.html', {'cities': cities, 'percentage': percentage})

def about(request):
    return render(request, 'sobre.html')