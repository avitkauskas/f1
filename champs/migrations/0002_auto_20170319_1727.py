# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'circuits',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'db_table': 'countries',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('last_car_no', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('last_model', models.CharField(blank=True, max_length=10)),
                ('active', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'db_table': 'drivers',
                'ordering': ['last_name', 'first_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'engines',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GPName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'GP name',
                'verbose_name_plural': 'GP names',
                'db_table': 'gpnames',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrandPrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_no', models.PositiveSmallIntegerField()),
                ('date_of_race', models.DateField(blank=True, null=True)),
                ('circuit_length', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('laps', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('best_lap_time', models.DurationField(blank=True, null=True)),
                ('comments_qual', models.TextField(blank=True, verbose_name='qualifying comments')),
                ('comments_race', models.TextField(blank=True, verbose_name='race comments')),
            ],
            options={
                'verbose_name': 'Grand Prix',
                'verbose_name_plural': 'Grand Prix',
                'db_table': 'gps',
                'ordering': ['champ_year', 'sequence_no'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_index_1', models.PositiveSmallIntegerField()),
                ('sort_index_2', models.PositiveSmallIntegerField()),
                ('model', models.CharField(blank=True, max_length=10)),
                ('car_no', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='car number')),
                ('laps', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('place_qual', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='qualifying place')),
                ('time_qual', models.DurationField(blank=True, null=True, verbose_name='qualifying time')),
                ('place_race', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='finishing place')),
                ('time_race', models.DurationField(blank=True, null=True, verbose_name='finishing time')),
                ('points', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('points_champ', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='championship points')),
                ('points_constructor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='constructor points')),
                ('points_champ_constructor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='constructor championship points')),
                ('set_fastest_lap', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'results',
                'ordering': ['gp__date_of_race', 'sort_index_1', 'sort_index_2'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Retirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'retirements',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'teams',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='champ',
            options={'managed': False, 'ordering': ['-year']},
        ),
    ]
