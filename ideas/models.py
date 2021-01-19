from django.db import models


class Idea(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None)
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(
        "tools.Tool", verbose_name="ideas", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Idea_detail", kwargs={"pk": self.pk})
