from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_viewer(request):
    form=LoginForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index_viewer')

            else:
                messages.error(request,'Incorrect Credentials')
                return redirect('login_viewer')   
    return render(request,'loginPage.html',{'form':form}) 


def registration_viewer(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

@login_required(login_url='/')
def index_viewer(request):
    return render(request,'index.html')   