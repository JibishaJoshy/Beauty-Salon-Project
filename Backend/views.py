from django.shortcuts import render,redirect
from Backend.models import CategoryDB,ProductDB
from Webapp.models import ContactDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here.
def index_page(request):
    return render(request,"index.html")

def Addcategory_page(request):
    return render(request,"Add_Category.html")

def savedata_Category(request):
    if request.method == "POST":
        na = request.POST.get('cg_name')
        des = request.POST.get('description')
        img = request.FILES['c_image']
        obj = CategoryDB(Category_Name=na,Description=des,Category_Image=img)
        obj.save()
        return redirect(Addcategory_page)

def Display_category(request):
    categ = CategoryDB.objects.all()
    return render(request,"Display_category.html",{'categ':categ})

def edit_category(request,Categoryid):
    categ = CategoryDB.objects.get(id=Categoryid)
    return render(request,"Edit_category.html",{'categ':categ})

def update_category(request,Categoryid):
    if request.method == "POST":
        na = request.POST.get('cg_name')
        des = request.POST.get('description')
        try:
            img = request.FILES['c_image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=Categoryid).Category_Image
        CategoryDB.objects.filter(id=Categoryid).update(Category_Name=na,Description=des,Category_Image=file)
        return redirect(Display_category)

def delete_category(request,Categoryid):
    x = CategoryDB.objects.filter(id=Categoryid)
    x.delete()
    return redirect(Display_category)

def AddProducts_page(request):
    categ = CategoryDB.objects.all()
    return render(request,"Add_Products.html",{'categ':categ})

def savedata_Products(request):
    if request.method == "POST":
        s_cat = request.POST.get('sel_category')
        p_na = request.POST.get('pr_name')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        img = request.FILES['pr_image']
        obj = ProductDB(Select_Category=s_cat, Product_Name=p_na, Price=pr, Description=des, Product_Image=img)
        obj.save()
        return redirect(AddProducts_page)

def display_Product(request):
    prod = ProductDB.objects.all()
    return render(request,"Display_Products.html",{'prod':prod})

def edit_products(request,Productid):
    prod = ProductDB.objects.get(id=Productid)
    categ = CategoryDB.objects.all()
    return render(request,"Edit_Products.html",{'prod':prod, 'categ':categ})

def update_products(request,Productid):
    if request.method == "POST":
        sel = request.POST.get('sel_category')
        na = request.POST.get('pr_name')
        des = request.POST.get('description')
        pr = request.POST.get('price')
        try:
            img = request.FILES['pr_image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=Productid).Product_Image
        ProductDB.objects.filter(id=Productid).update(Select_Category=sel,Product_Name=na,Description=des,Price=pr,Product_Image=file)
        return redirect(display_Product)

def delete_category(request,Categoryid):
    x = CategoryDB.objects.filter(id=Categoryid)
    x.delete()
    return redirect(Display_category)

# *************************************************************
def login_page(request):
    return render(request,"login.html")

def login_admin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)

            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(index_page)

            else:
                return redirect(login_page)
        else:
            return redirect(login_page)


def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)

# ******************************************************************

def Contact_Details(request):
    data = ContactDB.objects.all()
    return render(request,"Contactdata.html",{'data':data})

def delete_contact(request,Contactid):
    x = ContactDB.objects.filter(id=Contactid)
    x.delete()
    return redirect(Contact_Details)