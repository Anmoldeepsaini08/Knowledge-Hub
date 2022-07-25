from email.policy import default
from django.shortcuts import redirect, render
from django.http  import HttpResponse 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from matplotlib.style import use
from librarian.models import Books,Member
from django.shortcuts import resolve_url

def index(request):
	if request.method == 'POST':
		m_id = request.POST.get('mid')
		m_pass = request.POST.get('mpass')
		if Member.objects.filter(member_id = m_id).filter(member_pass=m_pass):
			#user = authenticate(request,username = m_id,password=m_pass)
			#login(request,user)
			return redirect('all')
		else: 	
			return redirect('library')
	else:
		return render(request,'member_login.html')


def all(request):

	if request.method == 'POST':
		print(request.POST.get('btn_issue'))	
		return redirect('all')	
	else:
		params ={}
		book = Books.objects.all()
		print(id)
		params = {'books' : book}
		#print(book)
		return render(request,'Library.html',params)

def applied(request):
	
	print(request.user)
	data = Books.objects.filter(branch_book = 'applied')
	
	return render(request,'Applied_science.html',{'books':data})

def cse(request):
	data = Books.objects.filter(branch_book = 'cse')
	return render(request,'Computer_science.html',{'books':data})

def mech(request):
	data = Books.objects.filter(branch_book = 'mechanical')
	return render(request,'Mechanical.html',{'books':data})

def ece(request):
	data = Books.objects.filter(branch_book = 'ece')
	return render(request,'Electronics.html',{'books':data})

def civil(request):
	data = Books.objects.filter(branch_book = 'civil')
	return render(request,'Civil.html',{'books':data})

def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('library')
    