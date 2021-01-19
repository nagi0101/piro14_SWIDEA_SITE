from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


# def idea_create(request, pk):
#     pass


class IdeaCreateView(CreateView):
    model = models.Idea
    fields = "__all__"


idea_create = IdeaCreateView.as_view()


# def idea_update(request, pk):
#     pass


class IdeaUpdateView(UpdateView):
    model = models.Idea
    fields = "__all__"
    template_name_suffix = "_update_form"


idea_update = IdeaUpdateView.as_view()


# def idea_delete(request, pk):
#     pass


class IdeaDeleteView(DeleteView):
    model = models.Idea
    success_url = reverse_lazy("ideas:idea_list")


idea_delete = IdeaDeleteView.as_view()