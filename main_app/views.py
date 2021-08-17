from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Art
# Create your views here.

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

arts = []
def arts_index(request):
  arts = Art.objects.all()
  return render(request, 'arts/index.html', { 'arts': arts })

def arts_detail(request, art_id):
  art = Art.objects.get(id=art_id)
  return render(request, 'arts/detail.html', { 'art': art })

class ArtCreate(CreateView):
  model = Art
  fields = '__all__'
  success_url = '/arts/'