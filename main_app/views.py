from django.shortcuts import render, redirect
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Art, Buyer
from .forms import ExhibitionForm
# Create your views here.

# Add the following import


class ArtCreate(LoginRequiredMixin, CreateView):
  model = Art
  fields = ['name', 'title', 'description', 'year']

  success_url = '/arts/'

  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class ArtUpdate(LoginRequiredMixin, UpdateView):
  model = Art
  # Let's disallow the renaming of a art by excluding the name field!
  fields = ['title', 'description', 'year']

class ArtDelete(LoginRequiredMixin, DeleteView):
  model = Art
  success_url = '/arts/'

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def arts_index(request):
  arts = Art.objects.filter(user=request.user)
  return render(request, 'arts/index.html', { 'arts': arts })

@login_required
def arts_detail(request, art_id):
  art = Art.objects.get(id=art_id)
  # Get the buyer the art doesn't have
  buyers_art_doesnt_have = Buyer.objects.exclude(id__in = art.buyers.all().values_list('id'))
  exhibition_form = ExhibitionForm()
  return render(request, 'arts/detail.html', { 'art': art, 'exhibition_form': exhibition_form, 'buyers': buyers_art_doesnt_have })

@login_required
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

class BuyerList(LoginRequiredMixin, ListView):
  model = Buyer

class BuyerDetail(LoginRequiredMixin, DetailView):
  model = Buyer

class BuyerCreate(LoginRequiredMixin, CreateView):
  model = Buyer
  fields = '__all__'

class BuyerUpdate(LoginRequiredMixin, UpdateView):
  model = Buyer
  fields = ['name', 'bid']

class BuyerDelete(LoginRequiredMixin, DeleteView):
  model = Buyer
  success_url = '/buyers/'

@login_required
def assoc_buyer(request, art_id, buyer_id):
  # Note that you can pass a buyer's id instead of the whole object
  Art.objects.get(id=art_id).buyers.add(buyer_id)
  return redirect('detail', art_id=art_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)