# Generated by Django 4.1.3 on 2022-11-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knigi', '0004_alter_books_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='janr',
            field=models.CharField(max_length=50, verbose_name='Жанр'),
        ),
    ]