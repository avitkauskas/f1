from django.http import HttpResponse
from django.shortcuts import render

from .models import Champ
from .models import GrandPrix


def years(request):
    years = Champ.objects.values_list('year', flat=True).order_by('year')
    rows = [[] for i in range(0, 10)]
    for year in years:
        rows[year % 10].append(year)
    context = {'rows': rows}
    return render(request, 'champs/years.html', context)


def champ(request, champ_year):
    gps = GrandPrix.objects.filter(champ_year=champ_year).order_by('sequence_no')
    context = {'gps': gps, 'year': champ_year}
    return render(request, 'champs/gps.html', context)
