from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect

from home.forms import CommentForm
from home.models import Category, Product, Customer_Comment


# Create your views here.

def index(request):
    # return HttpResponse("trang chu")
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/message_ok')

    context = {'form':form}

    return render(request, 'home/contact.html', context)

def tour(request):
    listCategory = Category.objects.all()

    products = Product.objects.all()

    return render(request,'home/tour.html',{'categories':listCategory,'products':products})

def productcat(request,id):
    listCategory = Category.objects.filter(cat_id=id)
    productCat = Product.objects.filter(cat_id=id)

    return render(request,'home/productcat.html',{'categories':listCategory,'productCat':productCat})

def productdetail(request, id):
    detail = Product.objects.get(pro_id=id)

    return render(request,'home/productdetail.html',{'detail':detail})

def message(request):
    return render(request, 'home/message.html')