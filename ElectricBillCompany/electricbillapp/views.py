from django.shortcuts import render
from .forms import *
from .models import *
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Create your views here.

def index(request):
    return render(request,'electricbillapp/index.html')

def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactUsForm()
    return render(request, 'electricbillapp/contactus.html',{'form':form})

def aboutus(request):
    return render(request, 'electricbillapp/aboutus.html')

def registeryourhouse(request):
    if request.method == 'POST':
        form = RegisterYourHouseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterYourHouseForm()
    return render(request,'electricbillapp/registeryourhouse.html',{'form':form})

def generatebill(request):
    if request.method == 'POST':
        form = GenerateBillForm(request.POST)
    else:
        form = GenerateBillForm()
    return render(request, 'electricbillapp/generatebill.html',{'form':form})

def generatebilldisplay(request):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)
    form = GenerateBillForm(request.POST)
    if form.is_valid():
        primarykey = form.cleaned_data['primarykey']
        bill = RegisterYourHouse.objects.get(pk=primarykey)
        units = form.cleaned_data['units']

        c.drawString(80,800,'Your Name : ')
        c.drawString(180, 800, bill.name)

        c.drawString(80, 750, 'Address : ')
        c.drawString(190, 750, bill.address)

        c.drawString(80, 700, 'Phone Number : ')
        phonenumber = str(bill.phonenumber)
        c.drawString(180,700, phonenumber)

        c.drawString(80,650, 'Postal Code : ')
        c.drawString(190, 650, bill.postalcode)

        c.drawString(80, 600, 'Meter Number : ')
        meternumber = str(primarykey)
        c.drawString(190, 600, meternumber)

        c.drawString(80, 550, 'Total Amount Due (CAD): ')
        unitcalculation = units*0.13
        unitstring = str(unitcalculation)
        c.drawString(220, 550, unitstring)
        c.showPage()
        c.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='electricitybill.pdf')

def addressdisplay(request):
    bill_all = RegisterYourHouse.objects.all()
    return render(request, 'electricbillapp/addressdisplay.html',{'bill_all':bill_all})


def backendportal(request):
    if request.method == 'POST':
        form = BackEndPortalForm(request.POST)
    else:
        form = BackEndPortalForm()

    return render(request, 'electricbillapp/backend/backendportal.html', {'form':form})

def backendportalextended(request):
    form = BackEndPortalForm(request.POST)
    valid = False
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        if username == 'admin' and password == 'root':
            valid = True
        else:
            valid = False

    return render(request, 'electricbillapp/backend/backendportalextended.html', {'valid':valid})

def backendindex(request):
    return render(request, 'electricbillapp/backend/backendindex.html')