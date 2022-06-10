from django.db import models
from datetime import datetime
# Create your models here.
class Library(models.Model):
    date_added = models.DateTimeField(default=datetime.now)
    bookname = models.CharField(max_length=100)
    bookauthor = models.CharField(max_length=100)
    payload = models.FileField(upload_to='media/library')
    category = models.CharField(max_length=50,default='Unknown')
    synopsis = models.CharField(max_length=1000,blank=True,null=True)
    #verbose_name_plural = 'Books'
    class Meta:
        verbose_name_plural = 'Books'

    def  get_queryset(self):
        return Library.objects.order_by('date_added') 
    
    def __str__(self):
        return self.bookname 
    