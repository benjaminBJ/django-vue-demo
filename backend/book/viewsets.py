from rest_framework import viewsets
from .models import Book,Page
from .serializer import BookSerializer,PageSerializer

#Clases para poder realizar CRUD

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer