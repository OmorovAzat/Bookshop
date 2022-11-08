from rest_framework import generics

from .models import *
from .serializers import *


class CategoryApiVew(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Booksapiview(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class AboutApiView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class HelpApiView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
