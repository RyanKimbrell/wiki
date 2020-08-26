from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random", views.random_page, name="random"),
    path("wiki/search", views.search, name="search"),
    path("wiki/new_page", views.create_new_page, name="new_page"),
    path("wiki/create", views.create, name="wiki/create"),
    path("wiki/save_edit", views.save_edit, name="wiki/save_edit"),
    path("wiki/edit/<str:title>", views.edit_page, name="edit"),
    path("wiki/<str:title>", views.display_entry, name="display_entry")
]
