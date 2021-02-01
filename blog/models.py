from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    objects = None
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=250, default=None, unique=False, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def __str__(self):
        return self.title


class Comentario(models.Model):
    author = models.CharField(max_length=200, null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    published_date = models.DateTimeField(blank=True, null=True)


# teste

#class Categoria(models.Model):
 #   nome = models.Charfield(max_length=100)
  #  dt_criacao = models.DateTimeField(auto_now_add=True)
