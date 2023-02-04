from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    Comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(default=now)

    def __str__(self):
        return f"On '{self.post.title}' commented by '{self.name}'"
