from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Category,Product

# Create your views here.

def index(request):
    # return HttpResponse("trang chu")
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')

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