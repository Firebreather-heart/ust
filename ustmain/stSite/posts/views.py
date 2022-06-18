from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic import DetailView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Article,Comment
from django import forms
from django.db.models import Q

# Create your views here.
class CustomCreateView(CreateView):
    class Meta:
        widget ={
            'title':forms.TextInput(attrs={
                'placeholder':'Title','class':'w3-input','type':'text'
            }),
            'body':forms.Textarea(attrs={
                'placeholder':'Body','class':'w3-input','type':'text'
            }),
            'comment':forms.TextInput(attrs={
                'placeholder':'Comment','class':'w3-input','type':'text','name':'comment','id':'comment',
            }),
            'id':forms.TextInput(attrs={
                'type':'hidden','value':Article.id 
            }),
        }

def display(request):
    if request.method == 'GET':
        img = Article.objects.order_by('-date')
        return render(request,'home.html',{'illustration':img})


def search_product(request):
     if request.method == 'GET':
        query= request.GET.get('q')
        print(query)
        
        if query is not None:
            lookups= Q(title__icontains=query) | Q(body__icontains=query)

            results= Article.objects.filter(lookups).distinct()

            return render(request, 'search_results.html', {'results':results})

        else:
            return render(request, 'search_results.html')

     else:
        return render(request, 'search_results.html')

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    fields =('title','body',)
    template_name = 'article_edit.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'
    context_object_name = 'object'
    
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
    fields = ('title', 'body','imgIllustration',)
    success_url = reverse_lazy('home')
    login_url = 'account_login'

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentView(LoginRequiredMixin,CustomCreateView):
    model = Comment 
    template_name ='comment.html'
    fields =('comment','id')
    success_url = reverse_lazy('article_detail')
    login_url = 'account_login'
    context_object_name = 'comment'

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)



class ArticleDetailView(LoginRequiredMixin,DetailView,):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'account_login'
    context_object_name = 'article_detail'

def commentView(request,pk):
    if request.POST:
        pass