from django.forms import ModelForm
from .models import Exhibition

class ExhibitionForm(ModelForm):
  class Meta:
    model = Exhibition
    fields = ['date', 'show']