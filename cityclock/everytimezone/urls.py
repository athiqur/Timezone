from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("change/", views.set_timezone, name="set_timezone"),
]
