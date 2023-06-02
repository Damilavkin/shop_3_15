from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    time_post = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name
