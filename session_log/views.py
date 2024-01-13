from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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
    queryset = Session.objects.order_by("-date")
    paginate_by = 5

    def get_queryset(self):
        """
        Retrieve the signed in user's logged sessions
        """
        return Session.objects.filter(author=self.request.user)  


class SessionDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Session.objects
        session = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "session_detail.html",
            {
                "session": session,
            },
        )
    
    def session(self, request, slug, *args, **kwargs):

        queryset = Session.objects
        session = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "session_detail.html",
            {
                "post": session,
            },
        )