from django.shortcuts import render,redirect
from AdminApp.models import categoryDB,productDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from datetime import datetime
from WebApp.models import contactDB,registerDB,orderDB,cartDB
from django.contrib import messages

# Create your views here.
def index(req):
    category=categoryDB.objects.count()
    product = productDB.objects.count()
    x=datetime.now()
    return render(req,"index.html",{'category':category,'product':product,'x':x})
def add_category(req):
    return render(req,"add_category.html")
def save_category(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('des')
        c=request.FILES['image']
        obj=categoryDB(cat_name=a,cat_des=b,cat_image=c)
        obj.save()
        messages.success(request,"category saved successfully...!")
        return redirect(add_category)
def display_category(req):
    cat_data=categoryDB.objects.all()
    return render(req,"display_category.html",{'cat_data':cat_data})
def edit_category(req,cat_id):
    cat_data=categoryDB.objects.get(id=cat_id)
    return render(req,"edit_category.html",{'cat_data':cat_data})
def update_category(req,cat_ID):
    if req.method=="POST":
        a = req.POST.get('name')
        b = req.POST.get('des')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categoryDB.objects.get(id=cat_ID).cat_image
        categoryDB.objects.filter(id=cat_ID).update(cat_name=a,cat_des=b,cat_image=file)
        messages.success(req, "category updated successfully...!")
        return redirect(display_category)
def delete_category(req,del_cat_ID):
    x=categoryDB.objects.filter(id=del_cat_ID)
    x.delete()
    messages.error(req, "category deleted...!")
    return redirect(display_category)

def add_product(req):
    category=categoryDB.objects.all()
    return render(req,"add_product.html",{'category':category})
def save_product(req):
    if req.method=="POST":
        a=req.POST.get('cat_name')
        b=req.POST.get('pro_name')
        c=req.POST.get('pro_price')
        d=req.POST.get('pro_des')
        e=req.POST.get('pro_quantity')
        f=req.FILES['image']
        obj=productDB(cat_name=a,pro_name=b,pro_price=c,pro_des=d,pro_quantity=e,pro_image=f)
        obj.save()
        messages.success(req, "product saved successfully...!")
        return redirect(add_product)

def display_product(req):
    pro_data=productDB.objects.all()
    return render(req,"display_product.html",{'pro_data':pro_data})
def edit_product(req,pro_id):
    category = categoryDB.objects.all()
    pro_data=productDB.objects.get(id=pro_id)
    return render(req,"edit_product.html",{'pro_data':pro_data,'category':category})
def update_product(req,pro_ID):
    if req.method=="POST":
        a = req.POST.get('cat_name')
        b = req.POST.get('pro_name')
        c = req.POST.get('pro_price')
        d = req.POST.get('pro_des')
        e = req.POST.get('pro_quantity')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productDB.objects.get(id=pro_ID).pro_image
        productDB.objects.filter(id=pro_ID).update(cat_name=a,pro_name=b,pro_price=c,pro_des=d,pro_quantity=e,pro_image=file)
        messages.success(req, "product updated successfully...!")
        return redirect(display_product)
def delete_product(req,del_pro_ID):
    x=productDB.objects.filter(id=del_pro_ID)
    x.delete()
    messages.error(req, "product deleted successfully...!")
    return redirect(display_product)
def admin_login_page(req):
    return render(req,"admin_login.html")
def admin_login(request):
    if request.method=="POST":
        un= request.POST.get('username')
        pwd= request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un, password=pwd)
            if x is not None:
                request.session['username']=un
                request.session['password'] = pwd
                login(request, x)
                messages.success(request, "Welcome to Bigmart Admin Dashboard...!")
                return redirect(index)
            else:
                messages.warning(request, "Invalid Password...!")
                return redirect(admin_login_page)
        else:
            messages.warning(request, "Invalid Username...!")
            return redirect(admin_login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Successfully Logout")
    return redirect(admin_login_page)
def contact_display(req):
    contact_data = contactDB.objects.all()
    return render(req, "contact_display.html", {'contact_data': contact_data})
def contact_delete(req,del_contact_ID):
    x=contactDB.objects.filter(id=del_contact_ID)
    x.delete()
    return redirect(contact_display)
def user_display(req):
    user_data = registerDB.objects.all()
    return render(req, "user_display.html", {'user_data': user_data})
def user_delete(req,del_user_ID):
    x=registerDB.objects.filter(id=del_user_ID)
    x.delete()
    return redirect(user_display)
def order_display(req):
    order_details=orderDB.objects.all()
    return render(req,"display_checkout.html",{'order_details':order_details})
def order_delete(req,del_order):
    x=orderDB.objects.filter(id=del_order)
    x.delete()
    messages.error(req, "User Details deleted successfully...!")
    return redirect(order_display)
def cart_display(req):
    cart_details=cartDB.objects.all()
    return render(req,"cart_details.html",{'cart_details':cart_details})





