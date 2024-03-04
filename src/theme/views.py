from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def page_not_found_view(request, exception):
  template = loader.get_template("theme/404.html")
  context = {}
  return HttpResponse(template.render(context, request))

