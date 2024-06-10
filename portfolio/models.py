from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    icon = models.FileField(upload_to='project_icons/')
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title
