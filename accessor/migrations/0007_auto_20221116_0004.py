# Generated by Django 4.1.3 on 2022-11-15 21:04

import time
import random
from django.db import migrations
from accessor.models import Stadium, SportType, Competition


def get_date(time_format, start_date, end_date):
    start_date = time.mktime(time.strptime(start_date, time_format))
    end_date = time.mktime(time.strptime(end_date, time_format))
    random_number = random.random()
    random_date = start_date + random_number * (end_date - start_date)
    date = time.strftime(time_format, time.localtime(random_date))
    return date


def fill_competition(apps, schema_editor):

    stadiums = Stadium.objects.all()
    sports = SportType.objects.all()

    for stadium, sport in zip(stadiums, sports):
        time_format = "%Y-%m-%d"

        start_date = get_date(time_format, "2022-5-1", "2022-5-15")
        end_date = get_date(time_format, "2022-5-16", "2022-5-30")

        Competition.objects.create(start_date=start_date,
                                   end_date=end_date, stadium=stadium, sport=sport)


class Migration(migrations.Migration):

    dependencies = [
        ('accessor', '0006_auto_20221115_2339'),
    ]

    operations = [
        migrations.RunPython(fill_competition)
    ]
