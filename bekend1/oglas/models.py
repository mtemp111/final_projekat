from django.db import models

# Create your models here.
class Oglas(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
 

    def __str__ (self):
        return self.title