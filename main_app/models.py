from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.
# Add the Art class & list and view function below the imports

SHOWS = (
    ('S', 'Somnyama Ngonyama'),
    ('W', 'WoA! Pt.2'),
    ('P', 'Paradigm of Charcoal')
)

class Buyer(models.Model):
  name = models.CharField(max_length=50)
  bid = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('buyers_detail', kwargs={'pk': self.id})

class Art(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    # Add the M:M relationaship
    buyers = models.ManyToManyField(Buyer)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id': self.id})
    
    def exhibited_for_today(self):
        return self.exhibition_set.filter(date=date.today()).count() >= len(SHOWS)



class Exhibition(models.Model):
  date = models.DateField('exhibition date')
  show = models.CharField(
    max_length=1,
	  choices=SHOWS,
	  default=SHOWS[0][0]
  )
  # Create a art_id FK
  art = models.ForeignKey(Art, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_show_display()} on {self.date}"
    
  # change the default sort
  class Meta:
    ordering = ['-date']