from django.shortcuts import render, redirect
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Art, Buyer
from .forms import ExhibitionForm
# Create your views here.

# Add the following import


class ArtCreate(CreateView):
  model = Art
  fields = '__all__'
  success_url = '/arts/'

class ArtUpdate(UpdateView):
  model = Art
  # Let's disallow the renaming of a art by excluding the name field!
  fields = ['title', 'description', 'year']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/arts/'

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

arts = []
def arts_index(request):
  arts = Art.objects.all()
  return render(request, 'arts/index.html', { 'arts': arts })

def arts_detail(request, art_id):
  art = Art.objects.get(id=art_id)
  # Get the buyer the art doesn't have
  buyers_art_doesnt_have = Buyer.objects.exclude(id__in = art.buyers.all().values_list('id'))
  exhibition_form = ExhibitionForm()
  return render(request, 'arts/detail.html', { 'art': art, 'exhibition_form': exhibition_form, 'buyers': buyers_art_doesnt_have })

def add_exhibition(request, art_id):
  # create a ModelForm instance using the data in request.POST
  form = ExhibitionForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the art_id assigned
    new_exhibition = form.save(commit=False)
    new_exhibition.art_id = art_id
    new_exhibition.save()
  return redirect('detail', art_id=art_id)

class BuyerList(ListView):
  model = Buyer

class BuyerDetail(DetailView):
  model = Buyer

class BuyerCreate(CreateView):
  model = Buyer
  fields = '__all__'

class BuyerUpdate(UpdateView):
  model = Buyer
  fields = ['name', 'bid']

class BuyerDelete(DeleteView):
  model = Buyer
  success_url = '/buyers/'

def assoc_buyer(request, art_id, buyer_id):
  # Note that you can pass a buyer's id instead of the whole object
  Art.objects.get(id=art_id).buyers.add(buyer_id)
  return redirect('detail', art_id=art_id)