from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    release_year = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2020)])
    company = models.CharField(max_length=20)
    description = models.TextField(max_length=512)
    avg_rating = models.FloatField(default=0)
    image = models.URLField(default=None)

    def __str__(self):
        return self.name

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username