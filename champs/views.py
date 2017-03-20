from django.http import HttpResponse
from django.shortcuts import render

from .models import Champ


def index(request):
    champs = Champ.objects.all()
    context = {'champs': champs}
    return render(request, 'champs/index.html', context)


def champ(request, champ_year):
    return HttpResponse('To be done yet.')
