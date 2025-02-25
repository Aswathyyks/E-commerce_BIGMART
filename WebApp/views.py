from django.shortcuts import render,redirect
from AdminApp.models import categoryDB,productDB
from WebApp.models import contactDB,registerDB,cartDB,orderDB
from django.contrib import messages
import razorpay

# Create your views here.
def home_page(req):
    total_item=0
    cart_data = cartDB.objects.filter(username=req.session['username'])
    for i in cart_data:
        total_item+=1



    category=categoryDB.objects.all()
    return render(req,"home.html",{'category':category,'cart_data':cart_data,'total_item':total_item})
def about(req):
    category = categoryDB.objects.all()
    return render(req,"about.html",{'category':category})
def contact(req):
    category = categoryDB.objects.all()
    return render(req,"contact.html",{'category':category})
def save_contact(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('phone')
        d=req.POST.get('subject')
        e=req.POST.get('message')
        obj=contactDB(name=a,email=b,phone=c,subject=d,message=e)
        obj.save()
        return redirect(contact)
def our_product(req):
    category = categoryDB.objects.all()
    product=productDB.objects.all()
    return render(req,"product.html",{'product':product,'category':category})
def filtered_product(req,category_name):
    category = categoryDB.objects.all()
    pro=productDB.objects.filter(cat_name=category_name)
    return render(req,"filtered_product.html",{'pro':pro,'category':category})
def single_product(req,pro_id):
    data=productDB.objects.get(id=pro_id)
    return render(req,"single_product.html",{'data':data})
def user_register(request):
    return render(request,"user_register.html")
def save_user_register(request):
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('pwd')
        e=request.POST.get('confirmpwd')
        if registerDB.objects.filter(username=a).exists():
            messages.warning(request,"Username already exists..!")
        elif registerDB.objects.filter(email=b).exists():
            messages.warning(request,"Email Id already exists..!")
        obj=registerDB(username=a,email=b,mobile=c,pwd=d,confirmpwd=e)
        obj.save()
        return redirect(user_register)
def user_login(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pwd=request.POST.get('password')
        if registerDB.objects.filter(username=un,pwd=pwd).exists():
            request.session['username'] = un
            request.session['pwd'] = pwd
            messages.success(request,"Welcome to Fruitikha...")
            return redirect(home_page)

        else:
            messages.warning(request, "Invalid Password...!")
            return redirect(user_register)
    else:
        messages.warning(request, "Invalid Username...!")
        return redirect(user_register)
def user_logout(request):
    del request.session['username']
    del request.session['pwd']
    messages.success(request, "Logout Successfully...")
    return redirect(user_register)
def cart(request):
    total_item = 0
    cart_data = cartDB.objects.filter(username=request.session['username'])
    for i in cart_data:
        total_item += 1
    sub_total=0
    shipping=0
    total=0
    category_data=categoryDB.objects.all()
    cart_data=cartDB.objects.filter(username=request.session['username'])
    for i in cart_data:
        sub_total+=i.total_price
        if sub_total>1000:
            shipping=100
        else:
            shipping=200
    total=sub_total+shipping
    return render(request,"cart.html",{'cart_data':cart_data,'category_data':category_data,'sub_total':sub_total,'shipping':shipping,'total':total,'total_item':total_item})
def save_cart(request):
    if request.method=="POST":
        pname=request.POST.get('pro_name')
        pprice = request.POST.get('price')
        pquantity = request.POST.get('pro_quantity')
        ptotal = request.POST.get('total')
        uname=request.POST.get('username')
        try:
            x=productDB.objects.get(pro_name=pname)
            img=x.pro_image
        except productDB.DoesNotExist:
            img=None
        obj=cartDB(pro_name=pname,quantity=pquantity,price=pprice,total_price=ptotal,pro_image=img,username=uname)
        obj.save()
        return redirect(home_page)
def delete_cart(req,del_ID):
    x=cartDB.objects.get(id=del_ID)
    x.delete()
    return redirect(cart)
def checkout_page(req):
    sub_total = 0
    shipping = 0
    total = 0
    cart_data=cartDB.objects.filter(username=req.session['username'])
    for i in cart_data:
        sub_total+=i.total_price
        if sub_total>1000:
            shipping=100
        else:
            shipping=200
    total=sub_total+shipping
    return render(req,"checkout.html",{'cart_data':cart_data,'sub_total':sub_total,'shipping':shipping,'total':total})
def save_checkout(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('address')
        d=req.POST.get('state')
        e=req.POST.get('phone')
        f=req.POST.get('pincode')
        g=req.POST.get('message')
        h=req.POST.get('total_price')
        obj=orderDB(name=a,email=b,address=c,state=d,phone=e,pincode=f,message=g,total_price=h)
        obj.save()
        return redirect(payment_page)
def payment_page(req):
    # retrieve data from orderDB with specified id
    customer=orderDB.objects.order_by('-id').first()

    pay=customer.total_price


    amount=int(pay*100)   #assuming the payment amount is RS,conveerting amount into paisa (smallest currency unit)
    pay_str=str(amount)  #converting into string

    if req.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_j9l2HpNNP23WVS', 'IuVw59pcVBL57PCewCWDup83'))
        payment=client.order.create({'amount':amount,'order_currency':order_currency})

    return render(req,"payment_page.html",{'customer':customer,'pay_str':pay_str})







