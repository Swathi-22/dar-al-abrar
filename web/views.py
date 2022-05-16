from django.shortcuts import render,get_object_or_404
from .models import Update
from .forms import ContactForm
from django.http import JsonResponse

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
    context ={
        "is_product" : True,
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