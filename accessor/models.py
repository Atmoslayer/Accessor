from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название команды')
    city = models.CharField(max_length=30, verbose_name='Город')
    players_quantity = models.IntegerField(verbose_name='Количество игроков')
    coach = models.CharField(max_length=30, verbose_name='Тренер')

    def __str__(self):
        return self.name


class Sportsman(models.Model):
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда')

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Result(models.Model):
    date = models.DateField(verbose_name='Дата выступления')
    attempt_number = models.IntegerField(verbose_name='Номер попытки')
    attempt_result = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Результат попытки')
    sportsman = models.ForeignKey(Sportsman, on_delete=models.CASCADE, verbose_name='Спортсмен')

    def __str__(self):
        return f'{self.sportsman.first_name} {self.sportsman.middle_name} {self.sportsman.last_name}'


class SportType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название вида спорта')

    def __str__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    capacity = models.IntegerField(verbose_name='Вместимость')

    def __str__(self):
        return self.name


class Competition(models.Model):
    sport = models.ForeignKey(SportType, on_delete=models.CASCADE, verbose_name='Спорт')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, verbose_name='Стадион')

    def __str__(self):
        return f'{self.sport.name} на стадионе {self.stadium.name}'
