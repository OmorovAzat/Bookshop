# Generated by Django 4.1.3 on 2022-11-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knigi', '0003_remove_books_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=20, verbose_name='Автор'),
        ),
    ]
