from django.urls import path 
from .views import LibraryView,BookUploadView,search_product,uploadbook

urlpatterns =[
    path('',LibraryView.as_view(),name='library'),
    path('upload',uploadbook,name='upload'),
    path('ls',search_product,name='librarysearch'),
]