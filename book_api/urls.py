
from django.contrib import admin
from django.urls import path
#call the view to be rendered, here we define the view we are gonna hit
from book_api.views import book_list, book_create,book

#define our path to render a webpage for us
urlpatterns = [
   path('',book_create),
   path('list/',book_list),
   path('<int:pk>', book)
   # at first we define the type,then the name(pk)
]



    #i want to hit this endpoint (books/list) and the endpoint 
    # should call this view right over here