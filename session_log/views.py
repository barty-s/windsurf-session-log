from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Session


def index(request):
    """
    Render the index.html template
    """
    return render(request, "index.html")


class SessionList(generic.ListView):
    """
    Render the users list of logged sessions
    """
    template_name = 'my_sessions.html'
    model = Session
    queryset = Session.objects.order_by("-created_on")
    paginate_by = 5

    def get_queryset(self):
        """
        Retrieve the signed in user's logged sessions
        """
        return Session.objects.filter(author=self.request.user)  
