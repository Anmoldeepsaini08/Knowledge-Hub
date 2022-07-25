from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='librarian'),
    path("addbooks/",views.addbooks,name='addbooks'),
    path("issuebookstatus/",views.issuebookstatus,name='issuebookstatus'),
    path("issuebook/",views.issuebook,name='issuebook'),
    path("returnbook/",views.returnbook,name='returnbook'),
    path("addmember/",views.addmember,name='addmember'),
    path('bookstatus/',views.bookstatus,name='bookstatus'),
    path("memberstatus/",views.memberstatus,name='memberstatus'),
    path('signout/',views.signout,name='signout')


   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)