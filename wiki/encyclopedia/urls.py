from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.getpage, name="title"),
    path("search", views.search, name="search")
]
