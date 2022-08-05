from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>ur NOT a total failure?????</h1>')

def about(request):
  return render(request, 'about.html')