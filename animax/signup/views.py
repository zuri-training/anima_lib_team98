from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render())

