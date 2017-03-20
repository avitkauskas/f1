from django.db import models


class Champ(models.Model):

    year = models.PositiveSmallIntegerField(
        unique=True,
    )

    comments_engine = models.TextField(
        'engine specs',
        blank=True,
    )

    comments_points = models.TextField(
        'points system',
        blank=True,
    )

    class Meta:
        db_table = 'champs'
        ordering = ['year']
        managed = False

    def __str__(self):
        return str(self.year)


class Country(models.Model):

    code = models.CharField(
        max_length=2,
    )

    name = models.CharField(
        max_length=20,
        unique=True,
    )

    class Meta:
        db_table = 'countries'
        ordering = ['name']
        verbose_name_plural = 'countries'
        managed = False

    def __str__(self):
        return "{} - {}".format(self.name, self.code)


class Circuit(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
    )

    country = models.ForeignKey(
        'Country', models.PROTECT,
        blank=True, null=True,
    )

    class Meta:
        db_table = 'circuits'
        ordering = ['name']
        managed = False

    def __str__(self):
        return "{} ({})".format(self.name, self.country.code)


class Engine(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
    )

    class Meta:
        db_table = 'engines'
        ordering = ['name']
        managed = False

    def __str__(self):
        return self.name


class Team(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
    )

    class Meta:
        db_table = 'teams'
        ordering = ['name']
        managed = False

    def __str__(self):
        return self.name


class Driver(models.Model):

    first_name = models.CharField(
        max_length=25,
        blank=True,
    )

    last_name = models.CharField(
        max_length=25,
    )

    country = models.ForeignKey(
        'Country', models.PROTECT,
        blank=True, null=True,
    )

    date_of_birth = models.DateField(
        blank=True, null=True,
    )

    date_of_death = models.DateField(
        blank=True, null=True,
    )

    last_car_no = models.PositiveSmallIntegerField(
        blank=True, null=True,
    )

    last_team = models.ForeignKey(
        'Team', models.PROTECT,
        blank=True, null=True,
        related_name='+',
    )

    last_engine = models.ForeignKey(
        'Engine', models.PROTECT,
        blank=True, null=True,
        related_name='+',
    )

    last_model = models.CharField(
        max_length=10,
        blank=True,
    )

    active = models.BooleanField(
        default=False,
        db_index=True,
    )

    class Meta:
        db_table = 'drivers'
        ordering = ['last_name', 'first_name']
        unique_together = ('last_name', 'first_name')
        managed = False

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Retirement(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    class Meta:
        db_table = 'retirements'
        ordering = ['name']
        managed = False

    def __str__(self):
        return self.name


class GPName(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
    )

    class Meta:
        db_table = 'gpnames'
        ordering = ['name']
        verbose_name = 'GP name'
        verbose_name_plural = 'GP names'
        managed = False

    def __str__(self):
        return self.name


class GrandPrix(models.Model):

    champ_year = models.ForeignKey(
        'Champ', models.PROTECT,
        db_column='champ_year',
        to_field='year',
    )

    sequence_no = models.PositiveSmallIntegerField()

    date_of_race = models.DateField(
        blank=True, null=True,
    )

    gpname = models.ForeignKey(
        'GPName', models.PROTECT,
        verbose_name='GP name',
        blank=True, null=True,
    )

    circuit = models.ForeignKey(
        'Circuit', models.PROTECT,
        blank=True, null=True,
    )

    circuit_length = models.DecimalField(
        max_digits=5, decimal_places=3,
        blank=True, null=True,
    )

    laps = models.PositiveSmallIntegerField(
        blank=True, null=True,
    )

    best_lap_time = models.DurationField(
        blank=True, null=True,
    )

    comments_qual = models.TextField(
        'qualifying comments',
        blank=True,
    )

    comments_race = models.TextField(
        'race comments',
        blank=True,
    )

    class Meta:
        db_table = 'gps'
        unique_together = ('champ_year', 'sequence_no')
        ordering = ['champ_year', 'sequence_no']
        verbose_name = 'Grand Prix'
        verbose_name_plural = 'Grand Prix'
        managed = False

    def __str__(self):
        return "{}:{:02d} {}".format(
            self.champ_year, self.sequence_no, self.gpname.name,
        )


class Result(models.Model):

    gp = models.ForeignKey(
        'GrandPrix', models.PROTECT,
        verbose_name='Grand Prix',
    )

    sort_index_1 = models.PositiveSmallIntegerField()

    sort_index_2 = models.PositiveSmallIntegerField()

    driver = models.ForeignKey(
        'Driver', models.PROTECT,
        blank=True, null=True,
    )

    team = models.ForeignKey(
        'Team', models.PROTECT,
        blank=True, null=True,
    )

    engine = models.ForeignKey(
        'Engine', models.PROTECT,
        blank=True, null=True,
    )

    model = models.CharField(
        max_length=10,
        blank=True,
    )

    car_no = models.PositiveSmallIntegerField(
        'car number',
        blank=True, null=True,
    )

    laps = models.PositiveSmallIntegerField(
        blank=True, null=True,
    )

    retirement = models.ForeignKey(
        'Retirement', models.PROTECT,
        verbose_name='retirement reason',
        blank=True, null=True,
    )

    place_qual = models.PositiveSmallIntegerField(
        'qualifying place',
        blank=True, null=True,
    )

    time_qual = models.DurationField(
        'qualifying time',
        blank=True, null=True,
    )

    place_race = models.PositiveSmallIntegerField(
        'finishing place',
        blank=True, null=True,
    )

    time_race = models.DurationField(
        'finishing time',
        blank=True, null=True,
    )

    points = models.DecimalField(
        max_digits=5, decimal_places=2,
        blank=True, null=True,
    )

    points_champ = models.DecimalField(
        'championship points',
        max_digits=5, decimal_places=2,
        blank=True, null=True,
    )

    points_constructor = models.DecimalField(
        'constructor points',
        max_digits=5, decimal_places=2,
        blank=True, null=True,
    )

    points_champ_constructor = models.DecimalField(
        'constructor championship points',
        max_digits=5, decimal_places=2,
        blank=True, null=True,
    )

    set_fastest_lap = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "results"
        unique_together = ("gp", "sort_index_1", "sort_index_2")
        ordering = ["gp__date_of_race", "sort_index_1", "sort_index_2"]
        managed = False

    def __str__(self):
        return "GP {}:{:02d} place {:02d}:{} {} {}".format(
            self.gp.champ_year, self.gp.sequence_no,
            self.sort_index_1, self.sort_index_2,
            self.driver.first_name, self.driver.last_name
        )
