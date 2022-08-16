from rest_framework import serializers
#we need to import the book model
from book_api.models import Book
#serializera convert data
# we need to tell the serializer what we want our data to be converted to(Which is usually json data)
# To do that we need to create our serializer object
 

#here we create our serializer object
class BookSerializer(serializers.Serializer):
    #here we are going to define the structure of the data we want in our json
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    number_of_pages = serializers.IntegerField()
    published_date = serializers.DateField() 
    quantity = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.published_date = data.get('published_date', instance.published_date)
        instance.quantity = data.get('quantity', instance.quantity)

        instance.save()
        return instance

#this is all we need to do to create out serializer

#here we need to create our create method, 
# This is the method that is going to called to create a book in our database

