from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:article-list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:article-list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:article-list')
