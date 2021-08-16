from django.db import models

# Create your models here.
# Add the Art class & list and view function below the imports

class Art(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name