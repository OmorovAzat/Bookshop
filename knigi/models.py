from django.db import models


class Category(models.Model):
    photobook = models.ImageField(verbose_name='Фото для книги')
    title = models.TextField(blank=True, verbose_name='Название книги')

    class Meta:
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.title


class Books(models.Model):
    bookcategory = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.CharField(max_length=20, verbose_name='Автор')
    janr = models.CharField(max_length=50, verbose_name='Жанр')
    sheet = models.CharField(max_length=25, blank=True, verbose_name='Кол-во страниц')
    lang = models.TextField(blank=True, verbose_name='Язык')
    pub_date = models.DateTimeField('Год выпуска')
    pricebook = models.IntegerField(blank=True, verbose_name='Цена')
    old_price = models.IntegerField(verbose_name='Старая Цена')
    pricediscount = models.IntegerField(verbose_name='Процент скидки')
    hitofsales = models.BooleanField(verbose_name='Хит продаж')
    newtov = models.BooleanField(verbose_name='Новинки')
    poiskizbrannye = models.BooleanField(verbose_name='Избранные')

    class Meta:
        verbose_name_plural = "Все книги"

    def __str__(self):
        return self.author


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Загаловок')
    imgus = models.ImageField(verbose_name='Фото о нас')

    class Meta:
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.title


class Help(models.Model):
    question = models.TextField(max_length=150, verbose_name='Вопрос')
    answer = models.TextField(max_length=150, verbose_name='Ответ')
    picture = models.ImageField(height_field=None, width_field=None,
                                max_length=100, verbose_name='Фото для помощи')

    class Meta:
        verbose_name_plural = "Помощь"

    def __str__(self):
        return self.question
