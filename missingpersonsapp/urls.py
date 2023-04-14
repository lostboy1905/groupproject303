from django.urls import path
from .views import indexPageView, contactPageView, BYUPageView, projectsPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("contact/", contactPageView, name="contact"),
    path("byu/", BYUPageView, name="byu"),
    path("projects/", projectsPageView, name="projects")
    ]