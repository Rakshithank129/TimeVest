from django.shortcuts import render,redirect
from userapp.forms import userForm,userFormProfile,UpdateForm,InvestmentForm
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        form = userForm(request.POST)
        profile = userFormProfile(request.POST,request.FILES)
        if form.is_valid() and profile.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            data1 = profile.save(commit=False)
            data1.user = user
            data1.save()
            registered = True
    else:

        form = userForm()
        profile = userFormProfile()
    context = {
        'form':form,
        'profile': profile,
        'registered' : registered
    }
    return render(request,'registration.html',context)

def user_login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user:
            if user.is_active:
                auth.login(request,user)
                return redirect("home")
        else:
            return HttpResponse("please check your creds...!!!")  
    return render(request,'login.html',{})

@login_required(login_url='login')
def home(request):
    return render(request,"home.html",{})

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html',{})


@login_required(login_url="login")
def user_logout(request):
    auth.logout(request)
    return redirect("login")


@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST,instance=request.user)
        if form.is_valid:
            form.save()
        return redirect('dashboard')
    else:
        form = UpdateForm(instance=request.user)
    return render(request,'update.html',{'form':form})

def investment_view(request):
    result = None
    if request.method == 'POST':
        form=InvestmentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            years_of_investment=form.cleaned_data['years_of_investment']
            amount=form.cleaned_data['amount']
            
            rate_of_return = 0.18
            final_amount = float(amount)*((1+rate_of_return)**float(years_of_investment))
            result ={
                'name':name,
                'age':age,
                'years_of_investment':years_of_investment,
                'initial_amount':amount,
                'final_amount':final_amount
            }
    else:
        form=InvestmentForm()
        
    return render(request,'investment.html',{'form':form,'result':result})



