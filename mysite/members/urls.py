from django.urls import path

from . import views

app_name = "members"

urlpatterns = [
    path("", views.ej1, name="ej1"),
    path("second/", views.second, name="second"),
]