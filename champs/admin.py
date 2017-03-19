from django.contrib import admin

from .models import Champ
from .models import Country
from .models import Circuit
from .models import Engine
from .models import Team
from .models import Driver
from .models import Retirement
from .models import GPName
from .models import GrandPrix
from .models import Result

admin.site.disable_action('delete_selected')


@admin.register(Champ)
class ChampAdmin(admin.ModelAdmin):
    search_fields = ['year']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    search_fields = ['last_name']

@admin.register(Retirement)
class RetirementAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(GPName)
class GPNameAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(GrandPrix)
class GrandPrixAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_of_race'
    search_fields = ['gpname__name']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    search_fields = ['driver__last_name']
