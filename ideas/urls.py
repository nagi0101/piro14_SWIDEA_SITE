from django.urls import path
from . import views

app_name = "ideas"

urlpatterns = [
    path("", views.idea_list, name="idea_list"),
    path("<int:pk>/", views.idea_detail, name="idea_detail"),
    path("<int:pk>/create", views.idea_create, name="idea_create"),
    path("<int:pk>/update", views.idea_update, name="idea_update"),
]
