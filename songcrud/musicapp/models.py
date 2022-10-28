from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=400, default = "null")
    last_name = models.CharField(max_length=400, default = "null")
    age = models.IntegerField(default = 30)

class Song(models.Model):
    title = models.CharField(max_length=400, default = "null")
    date_released = models.DateField(default = datetime.today)
    likes = models.IntegerField(default = 0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.CharField(max_length=400, default = "null")
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)