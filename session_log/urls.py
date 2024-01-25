from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("mysessions/", views.SessionList.as_view(), name="my_sessions"),
    path("createsession/", views.CreateSession.as_view(), name="create_session"),
    path("<slug:slug>/", views.SessionDetail.as_view(), name="session_detail"),
    path("update_session/<slug:slug>", views.UpdateSession.as_view(), name="update_session"),
    path("delete_session/<slug:slug>/delete", views.DeleteSession.as_view(), name="delete_session"),
    path('403/', views.handler403, name='handler403'),
    path('404/', views.handler404, name='handler404'),
    path('405/', views.handler405, name='handler405'),
    path('500/', views.handler500, name='handler500'),
]
