# Generated by Django 4.0.3 on 2022-05-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(default='', upload_to='librarian/images'),
        ),
    ]
