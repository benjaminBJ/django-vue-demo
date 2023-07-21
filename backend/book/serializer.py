from rest_framework import serializers
from .models import Book,Page

#Formatear clases para ser tratadas en formatos standard
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'