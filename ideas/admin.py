from django.contrib import admin
from . import models


@admin.register(models.Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ("title", "interest", "devtool")
