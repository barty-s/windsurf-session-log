from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from .models import Session
from .forms import SessionForm


def index(request):
    """
    Render the index.html template
    """
    return render(request, "index.html")


class SessionList(generic.ListView):
    """
    Render the user's list of logged sessions
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
    """
    Render the session details after the user clicks on one from the list
    """
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
   

class CreateSession(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    View for creating a new blog post
    """
    template_name = "create_session.html"
    model = Session
    form_class = SessionForm
    success_message = "Your session has been logged!"
    success_url = reverse_lazy("my_sessions")

    def form_valid(self, form):
        """
        Custom logic to handle form validation when creating a new blog post
        """
        form.instance.author_id = self.request.user.pk
        return super(CreateSession, self).form_valid(form)


class UpdateSession(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, generic.UpdateView):
    """
    View for updating a logged session
    """
    model = Session
    template_name = "update_session.html"
    form_class = SessionForm
    success_message = "Your session has been updated successfully!"
    success_url = reverse_lazy("my_sessions")

    def test_func(self):
        """
        Check if the current user is the author of the post being updated
        """
        session = self.get_object()
        return self.request.user == session.author


class DeleteSession(
    LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    View to delete a session
    """
    model = Session
    template_name = "delete_session.html"
    success_url = reverse_lazy("my_sessions")

    def test_func(self):
        """
        Check if the current user is the author of the post being deleted
        """
        session = self.get_object()
        return self.request.user == session.author


def handler403(request, exception=None):
    """
    Custom 403 page
    """
    return render(request, "403.html", status=403)


def handler404(request, exception=None):
    """
    Custom 404 page
    """
    return render(request, "404.html", status=404)


def handler405(request, exception=None):
    """
    Custom 405 page
    """
    return render(request, "405.html", status=405)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, "500.html", status=500)