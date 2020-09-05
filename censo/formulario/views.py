from django.shortcuts import render

from .forms import PostCityForm
from .models import Municipio, Mapeamento

def post_city(request):
    if request.method == 'POST':
        form = PostCityForm(request.POST)
        print(form.has_changed)
        if form.is_valid():
            form.save()
            return render(request, 'base.html')
    else:
        form = PostCityForm()
        form.fields['municipio'].queryset = Municipio.objects.filter(validacao=False)

    return render(request, 'form.html', {'form': form})