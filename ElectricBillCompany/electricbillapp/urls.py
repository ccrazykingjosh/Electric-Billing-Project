from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contactus', views.contactus, name='contactus'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('registeryourhouse', views.registeryourhouse, name='registeryourhouse'),
    path('generatebill', views.generatebill, name='generatebill'),
    path('generatebilldisplay', views.generatebilldisplay, name='generatebilldisplay'),
    path('addressdisplay', views.addressdisplay, name='addressdisplay'),
    path('backendportal', views.backendportal, name='backendportal'),
    path('backendportalextended', views.backendportalextended, name='backendportalextended'),
    path('backendindex', views.backendindex, name='backendindex')

]