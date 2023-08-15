from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    """create model for blogs"""
    blog = models.CharField(max_length=200)
    publish = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.blog


class Posts(models.Model):
    """create model for Posts"""
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    text = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.text
