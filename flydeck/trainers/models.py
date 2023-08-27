from django.db import models

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='trainers/')
    expertise = models.CharField(max_length=100)
    social_media = models.URLField(blank=True)

    def __str__(self):
        return self.name
