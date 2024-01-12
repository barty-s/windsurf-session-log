from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("mysessions/", views.SessionList.as_view(), name="my_sessions"),
]
