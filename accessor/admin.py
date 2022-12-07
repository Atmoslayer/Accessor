from django.contrib import admin
from .models import Team, Sportsman, Result, SportType, Competition, Stadium


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'players_quantity', 'coach']


@admin.register(Sportsman)
class SportsmanAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'team']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['date', 'attempt_number', 'attempt_result', 'sportsman']


@admin.register(SportType)
class SportTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['sport', 'start_date', 'end_date', 'stadium']


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'capacity']


