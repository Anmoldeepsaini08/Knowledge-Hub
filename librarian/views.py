from django.shortcuts import render,redirect
from .models import Books,Member,Issue_Book
from django.contrib.auth import authenticate,login,logout
# Create your views here.
import datetime

def index(request):
    if request.method == 'POST':
        lib_name = request.POST.get('uname')
        lib_pass = request.POST.get('pass')

        if lib_name == 'admin' and lib_pass == 'admin':
            return redirect('addbooks')

    return render(request,'librarian_login.html')

def addbooks(request):

    
    if request.method == 'POST':
        if Books.objects.filter(book_code = request.POST.get('bookcode')):
            return render(request,'librarian.html')
        else:
            book = Books()
            book.book_code = request.POST.get('bookcode')
        
            book.book_name= request.POST.get('bookname')
            book.author = request.POST.get('author')
            book.quantity = request.POST.get('quantity')
            book.branch_book =request.POST.get('branch')
            book.category = request.POST.get('category')
            
            book.image = request.FILES['image']
            book.save()
         
            return render(request,'librarian.html')
    else:
        return render(request,'librarian.html')

def issuebookstatus(request):
    data = Issue_Book.objects.all()

    return render(request,'issue_book_status.html',{'issuebookstatus': data})

def issuebook(request):
    if request.method == 'POST':
        if Books.objects.filter(book_code = request.POST.get('b_code')):
            quantity = Books.objects.filter(book_code = request.POST.get('b_code')).values_list('quantity')[0]
            #print(quantity[0])
            if quantity[0] > 0 :
                if Issue_Book.objects.filter(book_code_issue = request.POST.get('b_code')).filter(issue_id = request.POST.get('m_id')).filter(book_status = 'Pending'):
                    print('issued already')
                    return redirect('issuebook')
                else:
                    x = datetime.datetime.now()
                    date = x.strftime("%Y-%m-%d")
                    issue = Issue_Book()
                    #print(quantity)
                    issue.book_code_issue = request.POST.get('b_code')
                    issue.issue_id =  request.POST.get('m_id')
                    issue.book_status = 'Pending'
                    issue.date = date
                    issue.save()
                    return redirect('issuebook')
        else:
            return redirect('issuebook')

    else:
        return render(request,'issue_book.html')

def bookstatus(request):
    data = Books.objects.all()
    return render(request,'book_status.html',{'bookstatus': data})


def returnbook(request):
    if request.method == 'POST':
        if Issue_Book.objects.filter(book_code_issue = request.POST.get('r_b_id')).filter(issue_id = request.POST.get('r_m_id')):

            Issue_Book.objects.filter(book_code_issue = request.POST.get('r_b_id')).update(book_status = 'Returned')
            return redirect('returnbook')

        else:
            return redirect('returnbook')

    else:

        return render(request,'return_book.html')


def addmember(request):
    if request.method == 'POST':
        if Member.objects.filter(member_id = request.POST.get('mem_id')):
            return render(request,'add_member.html')
        else:
            member_add = Member()

            member_add.member_id = request.POST.get('mem_id')
            member_add.member_name = request.POST.get('mem_name')

            member_add.member_pass = request.POST.get('mem_name')
            member_add.save()
            return render(request,'add_member.html')
    else:
        return render(request,'add_member.html')


def memberstatus(request):
    data = Member.objects.all()
    return render(request,'member_status.html',{'memberstatus': data})
    
def signout(request):
    logout(request)
    return redirect('librarian')
    