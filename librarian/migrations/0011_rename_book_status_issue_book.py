# Generated by Django 4.0.3 on 2022-05-22 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0010_book_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book_Status',
            new_name='Issue_Book',
        ),
    ]