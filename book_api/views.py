#do avoid writing all this
#we are going to use the djano rest framework that has a serializer that 
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import JsonResponse
from rest_framework import status
from book_api.models import Book
from book_api.serializer import BookSerializer

# here in the views we are going to utilize the serializer to perform everything for us


# Create your views here., 
#the views are responsible for returning our data
# Since we are specifying rest_framework, we need to specify if this is a GET request or
# a POST request etc .. using the decorator, then here we will call 
# the api_viewon top of the function, in this case is a GET request
@api_view(['GET'])
def book_list(request):
    # serialize the data from complex data to json
    # here we get our books(all of them) in a complex data 
    # manner we gnneach book in the database is gonna be an object
    books = Book.objects.all() #gets datatype complex data
    #here we are going to pass in the complex data into this bookSerializer
    # let us assigin any variable,and pass in the book we got from pur database
    #(many=True)serialize many objects into json, because it will return a list of objects
    serializer = BookSerializer(books, many=True)
    #return rresponse
    return Response(serializer.data)

    # # convert the complex data (books to list)  to pythonLists
    # #get the value of each list
    # books_python = list(books.values()) # python data
    # #convert python data structure to json
    # # web interacts to the server through JSON
    # #return JsonResponse and pass a python dictionary
    # return JsonResponse(
    #     {
    #          'books':  books_python 
    #     }
    # )

# in the first function we wanted to hit the endpoint books/list to get our books
#Here we need to grab the data the user is goin to send us,
# coz this is post request, and we are creating data, 
# the user wants to create a book, he need to provide us with data,
# they will provide us inside of the request body, once we grab
# the rquest body that fromat is going to be in json.so we need 
# to convert the json data to complex data inorder to insert it inside our database, so we need to serialize the data from json to complex data
@api_view(['POST'])
def book_create(request):
    # here we only creating the instance
    serializer = BookSerializer(data=request.data)
#the user may add invalid data or data with incorrect datatypes, 
# so we need to validate data first before letting it enter our database
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
    else:
        return Response(serializer.errors)

#/books endpoint 

@api_view(['GET','PUT','DELETE'])
def book(request, pk): 
    #if we want to get a specific book, we need to check that okay when you hit this endpoint,
    # but the request method is equal 
    # grab the book we want to update
    book = Book.objects.get(pk=pk) 
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
#once we hit the endpoint /books/1 pk will be 1
#/books endpoint to get, update and delete the specific book at that index
    if request.method == 'PUT':
        #we will supply it with the data that the user is passing in, 
        #here we are passing in the instance and  that data we want to update it to
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#change status from 200 to 404