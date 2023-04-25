from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='/login/')
@allowedUsers(allowed_roles=['admin','staff'])
# @adminOnly
def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    total = Order.objects.all()
    tot = total.count()
    products = Product.objects.all()
    delivered = Order.objects.filter(status='Delivered')
    pending = Order.objects.filter(status='Pending')
    delivered = delivered.count() 
    pending = pending.count()
    return render(request,'home.html',{'Order':orders,'Customer':customer,'total':tot,'Product':products,'delivered':delivered,'pending':pending})

@login_required(login_url='/login/')
@allowedUsers(allowed_roles=['admin','staff','customer'])
def forgot(request):
    if request.method=="POST":
        # name = request.POST.get('forgotusername')
        name = request.user
        passw = request.POST.get('newpassword')
        change = User.objects.get(username=name)
        change.set_password(passw)
        change.save()
        return render(request,'login.html',{})
    return render(request,'forgot.html',{})


@login_required(login_url='/login/')
@allowedUsers(allowed_roles=['admin','staff','customer'])
def ordering(request,id,pid):
    u = Customer.objects.get(pk=id)
    product = Product.objects.get(pk=pid)

    order = Order()
    order.prod = product
    order.cust = u
    order.status = 'Pending'
    order.save()
    messages.info(request,'Order accepted')
    return redirect('/products/')


@login_required(login_url='/login/')
@allowedUsers(allowed_roles=['admin','staff'])
def customerPage(request,cid):
    customer = Customer.objects.get(pk=cid)
    orders = customer.order_set.all()
    orderCount = orders.count()
    delivered = Order.objects.filter(status='Delivered')
    pending = Order.objects.filter(status='Pending')
    return render(request,'customer.html',{'customer':customer,'orderCount':orderCount,'order':orders,'delivered':delivered,'pending':pending})


@login_required(login_url='/login/')
def productPage(request):
    products = Product.objects.all() 
    return render(request,'products.html',{'products':products})


@login_required(login_url='/login/')
def createCustomer(request):
    form = CustomerCreationForm()
    if request.method=="POST":
        saving = CustomerCreationForm(request.POST)
        saving.save()
        return redirect('/')
    return render(request,'customerForm.html',{'formCustomer':form})

@login_required(login_url='/login/')
@allowedUsers(allowed_roles=['admin','staff'])
def createOrder(request,id):
    #Filter menu/form
    myFilter = OrderFilter()

    OrderFormSet = inlineformset_factory(Customer,Order,fields=('prod','status'),extra=5)
    customer = Customer.objects.get(pk=id)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form = OrderForm(initial={'cust':customer})

    if request.method=='POST':
        formset = OrderFormSet(request.POST,instance=customer)

        # form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')


    return render(request,'orderForm.html',{'form':formset,'myFilter':myFilter})


@login_required(login_url='/login/')
@allowedUsers(allowed_roles=['admin','staff'])
def updateOrder(request,id):
    order = Order.objects.get(pk = id)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'orderForm.html',{'form':form})


@login_required(login_url='/login/')
@allowedUsers(allowed_roles=['admin','staff'])
def deleteOrder(request,delId):
    order = Order.objects.get(pk = delId)
    if request.method=="POST":
        order.delete()
        return redirect('/')    
    return render(request,'deleteOrder.html',{'order':order})

@unauthenticated_user
def loginPage(request):
    if request.method=="POST":
        name = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request,username=name,password=passw)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'UserName or Password is Incorrect')

    return render(request,'login.html',{})

@unauthenticated_user
def register(request):
    # form = UserCreationForm()
    form = RegisterForm()
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            name = request.POST.get('first_name')
            email = request.POST.get('email')
            c = Customer(user=user,name=name,email=email)
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            c.save()
            username = form.cleaned_data.get('username')
           
            messages.success(request,'Account Created for'+username)
            redirect('/login/')
        else:
            messages.error(request,'not valid try again')
    return render(request,'register.html',{'UserForm':form})

@login_required(login_url='/login/')
def loggingOUT(request):
    logout(request)
    return render(request,'login.html',{})