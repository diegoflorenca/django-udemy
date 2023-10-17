from django.urls import path
from . import views

urlpatterns = [
    # handle URLs containing a number
    path("<int:month>", views.monthly_challenge_by_number),
    # handle URLs containing a string
    path("<str:month>", views.monthly_challenge)
]
