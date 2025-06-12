from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.challenge_by_month_number),
    path("<str:month>", views.challenge_by_month, name="month-challenge"),
]
