from django.shortcuts import render

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
  return render(request, 'arts/index.html', { 'arts': arts })


class Art:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, title, description, year):
    self.name = name
    self.title = title
    self.description = description
    self.year = year

arts = [
  Art('Linda Smith', 'Crying Women', 'Water Paint', 1906),
  Art('Sachi Shah', 'Mona Lisa', 'What expression is she actually making', 1894),
  Art('Raven Garcia', 'Scenary', 'Seasons', 1994)
]