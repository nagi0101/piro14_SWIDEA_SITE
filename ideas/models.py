from django.db import models
from django.shortcuts import reverse
from config.utils import uuid_name_upload_to


class Idea(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=uuid_name_upload_to)
    content = models.TextField()
    interest = models.PositiveIntegerField(default=0)
    devtool = models.ForeignKey(
        "tools.Tool", on_delete=models.CASCADE, related_name="ideas"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ideas:idea_detail", kwargs={"pk": self.pk})
