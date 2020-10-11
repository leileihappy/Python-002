from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


from .form import LoginForm
from django.contrib.auth import authenticate,login,logout

def bootstrap(request):
    if request.user.is_authenticated:
        return render(request,'form1.html')
    else:
        return redirect('/login1')
    

def login1(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username = cd['username'],password = cd['password'])
            if user:
                login(request,user)
                return redirect('/bootstrap')
            else:
                return HttpResponse('用户密码错误')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'form.html', {'form': login_form})

def logout1(request):
    logout(request)
    return redirect('/login1')