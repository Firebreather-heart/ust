from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Library 
from django.views.generic import ListView
from django.views.generic.edit import CreateView 
from django.db.models import Q
from django import forms
# Create your views here.
class CustomCreateView(CreateView):
    class Meta:
        widget ={
            'bookname':forms.TextInput(attrs={
                'placeholder':'bookname','class':'w3-input','type':'text','id':'bookname','name':'bookname',
            }),
            'bookauthor':forms.TextInput(attrs={
                'placeholder':'bookauthor','class':'w3-input','type':'text','id':'bookauthor','name':'bookauthor',
            }),
            'payload':forms.FileField(),

            'category':forms.TextInput(attrs={
                'placeholder':'category','class':'w3-input','type':'text','name':'category','id':'category',
            }),
            'synopsis':forms.Textarea(attrs={
                'placeholder':'synopsis','class':'w3-input','type':'text','name':'synopsis','id':'synopsis',
            }),
        }

class LibraryView(ListView):
    template_name = 'library.html'
    model = Library
    context_object_name ='library'

class BookUploadView(CustomCreateView):
    template_name = 'upload.html'
    model = Library
    fields =('bookname','bookauthor','payload','category','synopsis',)
    success_url = reverse_lazy('library')

    def form_valid(self, form) :
        return super().form_valid(form)

def uploadbook(request):
    books = Library.objects.all()
    if request.method == 'POST':
        bookname = request.POST['bookname']
        bookauthor = request.POST['bookauthor']
        payload = request.POST['payload']
        category = request.POST['category']
        synopsis = request.POST['synopsis']
        try:
            bookitem = Library(bookname=bookname,bookauthor=bookauthor,payload =payload,category = category,synopsis=synopsis)
            bookitem.save()
            return render(request, 'library.html',{'library':books})
        except Exception as e:
            print(e)
            return render(request,'library.html',{'error':'could not upload book'})
    return render(request,'upload.html',)
    

def search_product(request):
     if request.method == 'GET':
        query= request.GET.get('q')
        #print(query)
        
        if query is not None:
            lookups= Q(bookname__icontains=query) | Q(bookauthor__icontains=query)

            results= Library.objects.filter(lookups).distinct()
            #print(results)

            return render(request, 'ls.html', {'results':results})

        else:
            return render(request, 'ls.html')

     else:
        #print('jagba')
        return render(request, 'ls.html')