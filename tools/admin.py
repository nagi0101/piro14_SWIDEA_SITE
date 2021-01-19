from django.contrib import admin
from . import models


@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ("name", "kind")
