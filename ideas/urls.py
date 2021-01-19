from django.urls import path
from . import views

app_name = "ideas"

urlpatterns = [
    path("", views.idea_list, name="idea_list"),
    path("<int:pk>/", views.idea_detail, name="idea_detail"),
]
