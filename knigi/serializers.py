from rest_framework import serializers

from .models import Category, Books, About, Help


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('photobook', 'title')


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('bookcategory', 'author', 'janr', 'sheet', 'lang', 'pub_date', 'pricebook', 'old_price', 'pricediscount', 'hitofsales', 'newtov', 'poiskizbrannye',)


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('title', 'imgus')


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('question', 'answer', 'picture')
