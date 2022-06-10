from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
import uuid
# Create your models here.

class Article(models.Model):
    id = models.UUIDField( 
                primary_key=True,
                default=uuid.uuid4,
                editable=False
                )
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=100000000000)
    date = models.DateTimeField(default= datetime.now)
    imgIllustration = models.ImageField(upload_to='media/',blank=True,null=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self): 
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(
            Article,
            on_delete=models.CASCADE,
            related_name='comment',
    )
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateTimeField(default= datetime.now)
    comment = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.comment
    def get_absolute_url(self): 
        return reverse('comment', args=[str(self.id)])
