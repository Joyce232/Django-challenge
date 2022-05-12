from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


def upload_to(instance, filename):
    return 'authors/{filename}'.format(filename=filename)


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    picture = models.ImageField(upload_to=upload_to, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='article', related_query_name='article')
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=80)
    summary = models.TextField()
    first_paragraph = models.TextField()
    body = models.TextField()

