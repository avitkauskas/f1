from django.http import HttpResponse
from django.shortcuts import render

from .models import Champ


def index(request):
    years = Champ.objects.values_list('year', flat=True).order_by('year')
    rows = [[] for i in range(0, 10)]
    for year in years:
        rows[year % 10].append(year)
    context = {'rows': rows}
    return render(request, 'champs/index.html', context)


def champ(request, champ_year):
    return HttpResponse('To be done yet.')
