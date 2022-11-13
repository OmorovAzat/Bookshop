from django.urls import path

from . import views
from .views import CategoryApiView, BooksapiView, AboutApiView, HelpApiView

urlpatterns = [
    path('api/category/', CategoryApiView.as_view()),
    path('api/books/', BooksapiView.as_view()),
    path('api/about/', AboutApiView.as_view()),
]