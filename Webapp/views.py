from django.shortcuts import render,redirect
from Backend.models import ProductDB,CategoryDB
# from .models import ServicePackage
from Webapp.models import ContactDB,RegisterDb,CartDb,OrderDb
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def homepage(request):
    categ = CategoryDB.objects.all()
    prod = ProductDB.objects.all()
    return render(request,"Home.html",{'categ':categ,'prod':prod})

def Aboutpage(request):
    categ = CategoryDB.objects.all()
    return render(request,"About.html",{'categ':categ})

def Workspage(request):
    categ = CategoryDB.objects.all()
    prod = ProductDB.objects.all()
    return render(request,"Works.html",{'prod':prod,'categ':categ})

def Contactpage(request):
    categ = CategoryDB.objects.all()
    return render(request,"Contacts.html",{'categ':categ})

def savedata_Contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        me = request.POST.get('message')
        obj = ContactDB(YourName=na,Email=em,Subject=sub,Message=me)
        obj.save()
        return redirect(Contactpage)

def Filtered_Services(request,categ_name):
    data = ProductDB.objects.filter(Select_Category=categ_name)
    return render(request,"Services_filtered.html",{'data':data})

def Single_Productpage(request,prod_id):
    data = ProductDB.objects.get(id=prod_id)
    cat = CategoryDB.objects.all()
    return render(request,"Singleproduct.html",{'data':data,'cat':cat})

def save_Cart(request):
    if request.method== "POST":
        na = request.POST.get('username')
        pr = request.POST.get('price')
        qty = request.POST.get('quantity')
        sn = request.POST.get('Product_name')
        obj = CartDb (Username=na,Quantity=qty,Price=pr,Servicename=sn)
        obj.save()
        return redirect(homepage)


def CartPage(request):
    cat = CategoryDB.objects.all()
    data = CartDb.objects.filter(Username=request.session['Username'])
    Subtotal = 0
    Total = 0
    Discount = 0

    for d in data:
        Subtotal = Subtotal + d.Price
        if Subtotal >= 500:
            Discount = 10
        else:
            Discount = 5
        Total = Subtotal  - Discount
    return render(request, "Cart.html",{'data': data, 'Subtotal': Subtotal, 'Discount': Discount, 'Total': Total,'cat': cat})

def delete_item(request,p_id):
    x = CartDb.objects.filter(id=p_id)
    x.delete()
    messages.success(request, "Item deleted successfully!")
    return redirect(CartPage)

def CheckOut(request):
    products = CartDb.objects.filter(Username=request.session['Username'])
    Subtotal = 0
    Total = 0
    Discount = 0

    for d in products:
        Subtotal = Subtotal + d.Price
        if Subtotal >= 500:
            Discount = 10
        else:
            Discount = 5
        Total = Subtotal - Discount
    return render(request,"Checkout.html",{'products':products,'Subtotal': Subtotal, 'Discount': Discount, 'Total': Total})

def SaveOrder(request):
    if request.method == "POST":
        na = request.POST.get('name')
        adr = request.POST.get('address')
        ph = request.POST.get('phone')
        em = request.POST.get('email')
        tot = request.POST.get('total')
        obj = OrderDb(Name=na,Address=adr,Phone=ph,EmailAddress=em,Total=tot)
        obj.save()
        return redirect(homepage)

# *******************************
def Booking_page(request):
    categ = CategoryDB.objects.all()
    return render(request,"Booking.html",{'categ':categ})
def Order_page(request):
    return render(request,"order.html")
# **********************
# def pricing_view(request):
#     packages = ServicePackage.objects.all()
#     return render(request, 'pricing.html', {'packages': packages})
# *********************************
def Registration_page(request):
    return render(request,"Register.html")

def save_Register(request):
    if request.method== "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pas = request.POST.get('pass')
        obj = RegisterDb(Username =na,Email=em,Password=pas)
        obj.save()
        return redirect(homepage)


def Loginpg(request):
    return render(request,"FrntndLogin.html")
def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if RegisterDb.objects.filter(Username=un,Password=pswd).exists():
            request.session['Username']=un
            request.session['Password'] = pswd
            messages.success(request,"Welcome")
            return redirect(homepage)

        else:
            messages.error(request,"Invalid Password...!")
            return redirect(Registration_page)
    else:
        return redirect(Registration_page)

def UserLogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(homepage)
