from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

# def tool_list(request):
#     return render(request, "tools/tool_list.html")


class ToolListView(ListView):
    model = models.Tool


tool_list = ToolListView.as_view()


# def tool_detail(request, pk):
#     ctx = {
#         "pk": pk,
#     }
#     return render(request, "tools/tool_detail.html", ctx)


class ToolDetailView(DetailView):
    model = models.Tool


tool_detail = ToolDetailView.as_view()


# def tool_create(request, pk):
#     pass


class ToolCreateView(CreateView):
    model = models.Tool
    fields = "__all__"


tool_create = ToolCreateView.as_view()


# def tool_update(request, pk):
#     pass


class ToolUpdateView(UpdateView):
    model = models.Tool
    fields = "__all__"
    template_name_suffix = "_update_form"


tool_update = ToolUpdateView.as_view()


# def tool_delete(request, pk):
#     pass


class ToolDeleteView(DeleteView):
    model = models.Tool
    success_url = reverse_lazy("tools:tool_list")


tool_delete = ToolDeleteView.as_view()