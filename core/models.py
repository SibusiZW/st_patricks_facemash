from django.db import models

# Create your models here.
class Face(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='faces/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Mash(models.Model):
    face = models.ForeignKey(Face, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)