from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models

# def idea_list(request):
#     return render(request, "ideas/idea_list.html")


class IdeaListView(ListView):
    model = models.Idea


idea_list = IdeaListView.as_view()


# def idea_detail(request, pk):
#     ctx = {
#         "pk": pk,
#     }
#     return render(request, "ideas/idea_detail.html", ctx)


class IdeaDetailView(DetailView):
    model = models.Idea


idea_detail = IdeaDetailView.as_view()


def idea_create(request, pk):
    pass


def idea_update(request, pk):
    pass


def idea_delete(request, pk):
    pass