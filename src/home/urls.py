from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
  path("", views.index, name="index"),
  path("about/", views.about, name="about"),
  path("donate/", views.donate, name="donate"),
  path("volunteer/", views.volunteer, name="volunteer"),
  path("privacy/", views.privacy, name="privacy"),
  path("questions-and-answers/",
       views.questions_and_answers,
       name="questions-and-answers"),
  path("contact/", views.contact, name="contact"),
  path("financials/", views.financials, name="financials"),
]
