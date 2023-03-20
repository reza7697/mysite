from django.db import models

# Create your models here.

class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=250)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(null=True)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)