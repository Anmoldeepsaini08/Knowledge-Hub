# Generated by Django 4.0.3 on 2022-05-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0004_alter_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
