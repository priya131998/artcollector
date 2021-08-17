from django.forms import ModelForm
from .models import Feeding

class ExhibitionForm(ModelForm):
  class Meta:
    model = Exhibition
    fields = ['date', 'show']