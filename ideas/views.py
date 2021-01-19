from django.shortcuts import render

# Create your views here.


def idea_list(request):
    return render(request, "ideas/idea_list.html")


def idea_detail(request, pk):
    ctx = {
        "pk": pk,
    }
    return render(request, "ideas/idea_detail.html", ctx)


def idea_create(request, pk):
    pass


def idea_update(request, pk):
    pass