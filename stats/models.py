from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)

class Game(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='game_pics')

class Results(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    score = models.BooleanField

class GamePlayer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    result = models.ForeignKey(Results, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    

    






