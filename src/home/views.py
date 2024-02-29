from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, world. You're at the triallocator.org homepage.")

def about(request):
  return HttpResponse("Hello, world. You're at the triallocator.org about page.")

def donate(request):
  return HttpResponse("Hello, world. You're at the triallocator.org donation page.")

def volunteer(request):
  return HttpResponse("Hello, world. You're at the triallocator.org volunteering page.")

def privacy(request):
  return HttpResponse("Hello, world. You're at the triallocator.org privacy page.")
