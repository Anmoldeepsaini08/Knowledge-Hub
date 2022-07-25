from distutils.command.upload import upload
from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.


class Books(models.Model):
    id = models.AutoField
    book_code = models.CharField(max_length=10)
    book_name = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    quantity = models.IntegerField()
    branch_book = models.CharField(max_length=10)
    category = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/')

class Member(models.Model):
    
    member_id  = models.IntegerField()
    member_name = models.CharField(max_length=20)
    member_pass = models.CharField(max_length=20)

class Librarian(models.Model):
   
    lib_name = models.CharField(max_length=20)
    lib_pass = models.CharField(max_length=20)



class Issue_Book(models.Model):
    issue_id =  models.IntegerField()
    book_code_issue = models.CharField(max_length=10)
    book_status = models.CharField(max_length=10)
    date = models.DateField(default='')
