from django.contrib import admin
from .models import Team, Sportsman, Result, SportType, Competition, Stadium


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'players_quantity', 'coach']
    list_filter = ['name', 'city', 'players_quantity', 'coach']
    search_fields = ['name', 'city', 'players_quantity', 'coach']


@admin.register(Sportsman)
class SportsmanAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'middle_name', 'team']
    list_filter = ['last_name', 'first_name', 'middle_name', 'team']
    search_fields = ['last_name', 'first_name', 'middle_name', 'team']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'attempt_number', 'attempt_result', 'sportsman']
    list_filter = ['date', 'attempt_number', 'attempt_result', 'sportsman']
    search_fields = ['date', 'attempt_number', 'attempt_result', 'sportsman']


@admin.register(SportType)
class SportTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'sport', 'start_date', 'end_date', 'stadium']
    list_filter = ['sport', 'start_date', 'end_date', 'stadium']
    search_fields = ['sport', 'start_date', 'end_date', 'stadium']


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'capacity']
    list_filter = ['name', 'address', 'capacity']
    search_fields = ['name', 'address', 'capacity']
