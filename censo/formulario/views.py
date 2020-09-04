from django.shortcuts import render

from .forms import PostCityForm

def post_city(request):
    form = PostCityForm()
    return render(request, 'form.html', {'form': form})
