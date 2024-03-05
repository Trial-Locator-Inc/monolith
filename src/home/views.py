from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
  template = loader.get_template("home/index.html")
  context = {}
  return HttpResponse(template.render(context, request))

def about(request):
  template = loader.get_template("home/about.html")
  context = {}
  return HttpResponse(template.render(context, request))

def donate(request):
  template = loader.get_template("home/donate.html")
  context = {}
  return HttpResponse(template.render(context, request))

def volunteer(request):
  template = loader.get_template("home/volunteer.html")
  context = {}
  return HttpResponse(template.render(context, request))

def privacy(request):
  return HttpResponse("Hello, world. You're at the triallocator.org privacy page.")

def questions_and_answers(request):
  template = loader.get_template("home/q-and-a.html")
  context = {}
  return HttpResponse(template.render(context, request))

def contact(request):
  template = loader.get_template("home/contact.html")
  context = {}
  return HttpResponse(template.render(context, request))

def financials(request):
  template = loader.get_template("home/financials.html")
  context = {}
  return HttpResponse(template.render(context, request))

