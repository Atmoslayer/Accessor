# Generated by Django 4.1.3 on 2022-11-14 22:25
import random
from django.db import migrations


def fill_team(apps, schema_editor):
    team = apps.get_model('accessor', 'Team')

    names = [
        'Легенды о молниях', 'Отряд', 'Нарушители правил', 'Доминанта', 'Пуленепробиваемый', 'Портретный',
        'Братья Ниндзя', 'Большие Выстрелы', 'Мстители', 'Непреодолимая сила', 'Рожденный побеждать',
        'Лига Справедливости', 'Лучшие в игре'
    ]

    cities = [
        'Абинск', 'Москва', 'Ярославль', 'Тула', 'Сочи', 'Ростов Великий', 'Дмитров', 'Тверь', 'Рязань',
        'Екатеринбург', 'Воронеж', 'Владимир', 'Волгоград', 'Казань'
    ]

    coaches = [
        'Павлов', 'Козлов', 'Степанов', 'Николаев', 'Орлов', 'Андреев', 'Макаров', 'Никитин', 'Захаров',
        'Зайцев', 'Соловьев', 'Борисов', 'Яковлев', 'Григорьев', 'Романов', 'Воробьев'
    ]

    for quantity in range(15):
        team.objects.create(name=random.choice(names), city=random.choice(cities),
                            players_quantity=random.randint(1, 12), coach=random.choice(coaches))


class Migration(migrations.Migration):

    dependencies = [
        ('accessor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_team)
    ]