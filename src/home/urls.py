from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("about/", views.about, name="about"),
  path("donate/", views.donate, name="donate"),
  path("volunteer/", views.volunteer, name="volunteer"),
  path("privacy/", views.privacy, name="privacy"),
]