from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("mysessions/", views.my_sessions, name="my_sessions"),
]
