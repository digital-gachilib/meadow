# Generated by Django 3.0.5 on 2020-04-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("meadow", "0004_auto_20200421_1906")]

    operations = [migrations.AlterField(model_name="book", name="isbn_10", field=models.IntegerField())]
