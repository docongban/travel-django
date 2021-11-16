from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect

from home.forms import CommentForm, BookForm
from home.models import Category, Product, Customer_Comment, booktour
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    # return HttpResponse("trang chu")
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/message_ok')

    return render(request,'home/index.html', {'form':form})

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

cart={}
def addcart(request):
    if request.is_ajax():
        id=request.POST.get('id')
        # yourname=request.POST.get('your_name')
        # yourmail=request.POST.get('your_mail')
        # yourphone=request.POST.get('your_phone')
        # address=request.POST.get('add_ress')
        # number=request.POST.get('num')

        proDetail=Product.objects.get(pro_id=id)
        iteamCart={
            'name':proDetail.pro_name,
            'price':proDetail.pro_price,
            'image':proDetail.pro_image,
        }
        cart[id]=iteamCart
        request.session['cart']=cart
        cartInfo=request.session['cart']
        html= render_to_string('home/addcart.html', {'cart': cartInfo})  
    return HttpResponse(html)

def booknow(request, id): 
    detail = Product.objects.get(pro_id=id)
    form = BookForm()

    if request.method == 'POST':
        form =  BookForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'home/booknow.html', {'detail':detail,'form': form})