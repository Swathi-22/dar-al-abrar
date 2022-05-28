from email import message
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from .models import Category, Product, Update,Order,OrderUpdate
from .forms import ContactForm
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json

# Create your views here.
def index(request):
    updates=Update.objects.all().order_by('-id')[:3]
    context ={
        "is_index" : True,
        'updates':updates
    }
    return render(request,'web/index.html',context)



def service(request):
    context ={
        "is_service" : True,
    }
    return render(request,'web/service.html',context)



def product(request):
    category=Category.objects.all()
    context ={
        "is_product" : True,
        'category':category

    }
    return render(request,'web/product.html',context)



def updates(request):
    updates=Update.objects.all()
    context ={
        "is_update" : True,
        'updates':updates
    }
    return render(request,'web/blog.html',context)



def updatesDetails(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.all()
    context ={
        'updates':updates,
        'update':update
    }
    return render(request,'web/blog-details.html',context)



def contact(request):
    forms=ContactForm(request.POST or None)
    context ={
        "is_contact" : True,
        'forms':forms
    }
    return render(request,'web/contact.html',context)



def SaveContactForm(request):
  
    forms=ContactForm(request.POST or None)
    if request.method=='POST':
        if forms.is_valid():
            forms.save()
    return JsonResponse({'title':'name'})


def get_product(request):
    categoryId = request.POST['category']
    categoryname=Category.objects.get(id=categoryId)
    category=Product.objects.filter(category=categoryId)
    country=[]
    for i in category:
        data = {'name':i.countries.name}
        country.append(data)
    return JsonResponse({'data':country,'category':categoryname.title})
      


def get_price(request):
    categoryId=request.POST['category']
    countryId=request.POST['country']
    country=Product.objects.get(category=categoryId,countries__name=countryId)
    return JsonResponse({'price':country.price_for_one_TON})



def get_totalPrice(request):
    quantity=request.POST['quantity']
    price=request.POST['price']
    print(price)
    total_price=int(quantity)*int(price)
    return JsonResponse({'totalPrice':total_price})


def sendWhatsapp(request):
    print(request.POST)
    data = json.loads(request.POST['data'])
    name= request.POST['name']
    total= request.POST['total']
    companyname= request.POST['companyname']
    companyaddress= request.POST['companyaddress']
    email= request.POST['email']
    mobile= request.POST['mobile']
    messagestring = 'https://wa.me/9539438918?text=Name :'+name+'%0aCompany Name :'+companyname+'%0aCompany Address :'+companyaddress+'%0aEmail Id:'+email+'%0aMobile Number:'+mobile+\
                "%0a-----Order Details------"

    for i in data:
        messagestring +="%0aProduct:"+str(i['prdctName'])+"%0aCountry:"+str(i['country'])+"%0aQuantity:"+str(i['quantity'])+"%0aPrice:"+str(i['price'])+"%0a-----------------------------"
    messagestring+="%0a-----------------------------%0a\
    Grand Total :"+str(total)+"%0a--------------------------------"
    
    return JsonResponse({'link':messagestring})



def tracking(request):
    if request.method=='GET':
        code =request.GET.get('code',None)
        if Order.objects.filter(track_number=code).exists():
            order=Order.objects.filter(track_number__icontains=code).first()
        else:
            order = None
    context = {
        'order':order
    }
    return render(request,'web/track.html',context)



def live_tracking(request,slug):
    order=get_object_or_404(Order,track_number=slug)
    context ={
        'order':order
    }
    return render(request,'web/track.html',context)

   
       