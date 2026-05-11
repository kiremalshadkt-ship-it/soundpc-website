from django.db import models

# Create your models here.


class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='series/', blank=True)

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='characters')
    description = models.TextField()
    image = models.ImageField(upload_to='characters/', blank=True)
    role = models.CharField(max_length=50, choices=[('Hero', 'Hero'), ('Villain', 'Villain'), ('Sidekick', 'Sidekick')])

    def __str__(self):
        return self.name