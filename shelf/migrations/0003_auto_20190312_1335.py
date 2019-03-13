# Generated by Django 2.1.7 on 2019-03-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20190311_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='shelf.Author'),
        ),
    ]