from django.db import models

# Create your models here.
class HollywoodMovie(models.Model):
    title = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    actress = models.CharField(max_length=50)
    release_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class BollywoodMovie(models.Model):
    title = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    actress = models.CharField(max_length=50)
    release_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title