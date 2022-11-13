from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication

from .models import Category, Books, About, Help
from .serializers import CategorySerializer, BooksSerializer, AboutSerializer, HelpSerializer


class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class BooksapiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


class AboutApiView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class HelpApiView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
