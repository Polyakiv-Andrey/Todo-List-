from django.db import models


class Tags(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tag}"


class Task(models.Model):
    content = models.TextField()
    time_creation = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags)

    class Meta:
        ordering = ["status", "time_creation"]
