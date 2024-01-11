from django.shortcuts import render 
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Session
from django.contrib.auth.decorators import login_required


def index(request):
    """
    Render the index.html template
    """
    return render(request, "index.html")


@login_required
def my_sessions(request):
    """
    Render the my_sessions.html template with user's logged training sessions
    """
    user = request.user
    user_sessions = Session.objects.filter(author=user)

    return render(request, "my_sessions.html", {"user_session":user_sessions},)
