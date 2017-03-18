from django.db import models


class Champ(models.Model):
    year = models.PositiveSmallIntegerField(unique=True)
    comments_engine = models.TextField(blank=True)
    comments_points = models.TextField(blank=True)

    class Meta:
        db_table = "champs"
        managed = False
