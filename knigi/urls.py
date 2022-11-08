from django.urls import path

from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('api/category/', CategoryApiView.as_view()),
]