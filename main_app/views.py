from django.shortcuts import render
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art
from .forms import ExhibitionForm
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
  exhibition_form = ExhibitionForm()
  return render(request, 'arts/detail.html', { 'art': art, 'exhibition_form': exhibition_form })

class ArtCreate(CreateView):
  model = Art
  fields = '__all__'
  success_url = '/arts/'

class ArtUpdate(UpdateView):
  model = Art
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['title', 'description', 'year']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/arts/'