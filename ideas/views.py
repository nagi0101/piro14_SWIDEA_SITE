from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import json

from . import models


def idea_list(request):
    if request.method == "POST":
        pk = request.POST.get("pk", None)
        plus = int(request.POST.get("plus"))
        idea = get_object_or_404(models.Idea, pk=pk)
        if not (plus == -1 and idea.interest <= 0):
            models.Idea.objects.filter(pk=pk).update(interest=idea.interest + plus)
        ctx = {
            "idea_interest": get_object_or_404(models.Idea, pk=pk).interest,
        }
        return HttpResponse(json.dumps(ctx), content_type="application/json")
    else:
        posts = models.Idea.objects.all()
        ctx = {
            "posts": posts,
        }
        return render(request, "ideas/idea_list.html", ctx)


# class IdeaListView(ListView):
#     model = models.Idea


# idea_list = IdeaListView.as_view()


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