from django.contrib import admin

from .models import Article,Comment,ArticlePrime,Profile
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines =[
        CommentInline,
    ]
admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticlePrime)
admin.site.register(Profile)