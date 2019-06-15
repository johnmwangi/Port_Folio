from django.db import models


class User(models.Model):
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.image

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to = 'images/')
    github_url = models.URLField(blank=True)
    languages = models.TextField(blank=True)
    date = models.DateField(auto_now_add = False)


    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        Project.objects.filter().delete()

    @classmethod
    def get_all(cls):
        projects = Project.objects.all()
        return projects

    class Meta:
        ordering = ['-id']
