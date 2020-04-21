# Generated by Django 3.0.5 on 2020-04-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("meadow", "0003_book_isbn_10")]

    operations = [
        migrations.AlterField(model_name="book", name="isbn_10", field=models.IntegerField(unique=True)),
        migrations.AlterField(model_name="book", name="isbn_13", field=models.CharField(max_length=15, unique=True)),
    ]
