from django.shortcuts import render,get_object_or_404
from .models import Update

# Create your views here.
def index(request):
    context ={
        "is_index" : True,
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
    context ={
        "is_contact" : True,
    }
    return render(request,'web/contact.html',context)



