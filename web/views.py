from django.shortcuts import render

# Create your views here.
def index(request):
    context ={

    }
    return render(request,'web/index.html',context)



def service(request):
    context ={

    }
    return render(request,'web/service.html',context)



def product(request):
    context ={

    }
    return render(request,'web/product.html',context)



def updates(request):
    context ={

    }
    return render(request,'web/blog.html',context)



def updatesDetails(request):
    context ={

    }
    return render(request,'web/blog-details.html',context)



def contact(request):
    context ={

    }
    return render(request,'web/contact.html',context)



