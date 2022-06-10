from django.urls import path 
from .views import LibraryView,BookUploadView,search_product

urlpatterns =[
    path('',LibraryView.as_view(),name='library'),
    path('upload',BookUploadView.as_view(),name='upload'),
    path('ls',search_product,name='librarysearch'),
]