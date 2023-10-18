from django.urls import path
from . import views

urlpatterns = [
    # handle /challenges/ calls
    path("", views.index),
    # handle URLs containing a number
    path("<int:month>", views.monthly_challenge_by_number),
    # handle URLs containing a string
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
