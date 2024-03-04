from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
  template = loader.get_template("home/index.html")
  context = {}
  return HttpResponse(template.render(context, request))

def about(request):
  return HttpResponse("Hello, world. You're at the triallocator.org about page.")

def donate(request):
  return HttpResponse("Hello, world. You're at the triallocator.org donation page.")

def volunteer(request):
  return HttpResponse("Hello, world. You're at the triallocator.org volunteering page.")

def privacy(request):
  return HttpResponse("Hello, world. You're at the triallocator.org privacy page.")
