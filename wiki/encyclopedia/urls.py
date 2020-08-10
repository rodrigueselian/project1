from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.getpage, name="title"),
    path("search/", views.search, name="search"),
    path("new/", views.newpage, name="new"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("random/", views.rand, name="rand")
]
