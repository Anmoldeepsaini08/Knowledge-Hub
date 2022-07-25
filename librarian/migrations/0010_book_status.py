# Generated by Django 4.0.3 on 2022-05-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0009_librarian'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_name', models.CharField(max_length=20)),
                ('issue_id', models.IntegerField()),
                ('book_code_issue', models.CharField(max_length=10)),
                ('book_status', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
