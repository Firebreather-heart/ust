from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Article,Comment
from django import forms

# Create your views here.
class CustomCreateView(CreateView):
    class Meta:
        widgets ={
            'title':forms.TextInput(attrs={
                'placeholder':'Title','class':'w3-input','type':'text'
            }),
            'body':forms.Textarea(attrs={
                'placeholder':'Body','class':'w3-input','type':'text'
            }),
            'comment':forms.TextInput(attrs={
                'placeholder':'Comment','class':'w3-input','type':'text'
            })
        }

def display(request):
    if request.method == 'GET':
        img = Article.objects.order_by('-date')
        return render(request,'home.html',{'illustration':img})

def search_product(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Article.objects.filter(name__contains=query_name)
            return render(request, 'search_results.html', {"results":results})

    return render(request, 'search_results.html')

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    fields =('title','body',)
    template_name = 'article_edit.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    
    def dispatch(self, request, *args, **kwargs) :
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article 
    template_name ='article_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    def dispatch(self, request, *args, **kwargs) :
        obj = self.get_object()
        if obj.author!= self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin,CustomCreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body','imgIllustration')
    success_url = reverse_lazy('home')
    login_url = 'account_login'

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentView(LoginRequiredMixin,CustomCreateView):
    model = Comment 
    template_name = 'comment.html'
    fields =('comment',)
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    context_object_name = 'comment'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'account_login'
    context_object_name = 'article_detail'