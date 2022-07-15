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
    date = models.DateTimeField(default=datetime.now())
    imgIllustration = models.FileField(upload_to='media/',default='media/logo.jpg')
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=1)

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self): 
        return reverse('article_detail', args=[str(self.id)])

class ArticlePrime(models.Model):
    id = models.UUIDField( 
                primary_key=True,
                default=uuid.uuid4,
                editable=False
                )
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=100000000000)
    date = models.DateTimeField(default=datetime.now())
    imgIllustration = models.FileField(upload_to='media/',default='media/logo.jpg')

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Article of the week'
    

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

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    profile_pic = models.FileField(upload_to='media/profiles/',default='media/profiles/img_avatar2.png')
    age = models.SmallIntegerField()
    address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__('profile')