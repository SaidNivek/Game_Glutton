from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True)
    bgg_id = models.IntegerField(blank = True, null = True)
    thumbnail = models.CharField(max_length=250, blank = True, null = True)
    img = models.CharField(max_length=250, blank = True, null = True)
    description = models.CharField(max_length=1000, blank = True, null = True)
    year_published = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.name

class TrendingGame(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True)
    bgg_id = models.IntegerField(blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    thumbnail = models.CharField(max_length=250, blank = True, null = True)
    year_published = models.IntegerField(blank = True, null = True)