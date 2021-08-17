from django.db import models
from django.urls import reverse

# Create your models here.
# Add the Art class & list and view function below the imports

SHOWS = (
    ('S', 'Somnyama Ngonyama'),
    ('W', 'WoA! Pt.2'),
    ('P', 'Paradigm of Charcoal')
)

class Art(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id': self.id})



class Exhibition(models.Model):
  date = models.DateField('exhibition date')
  show = models.CharField(
    max_length=1,
	 choices=SHOWS,
	 default=SHOWS[0][0]
  )
  # Create a cat_id FK
  art = models.ForeignKey(Art, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_show_display()} on {self.date}"
    
    