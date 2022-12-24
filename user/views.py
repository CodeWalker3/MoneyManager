from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http.response import  HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1',False)
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Esse usuario ja existe')
        if user is None:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('login')

        return render(request, 'cadastro.html')



def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

@login_excluded('index')
def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def signout(request):
    if request.method == 'GET':
        logout(request)
    return redirect(reverse('index'))