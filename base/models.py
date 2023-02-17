from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255,default='My Blog')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.author)
    