from django.db import models


class Column (models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=20, blank=True, default="filter_none")
    palette = models.CharField(max_length=20, blank=True, default="kanban To-do")

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    palette = models.CharField(max_length=20, blank=True)
    link = models.URLField(max_length=100, blank=True)
    attachment = models.FileField(upload_to="files", blank=True)

    def __str__(self):
        return self.title 