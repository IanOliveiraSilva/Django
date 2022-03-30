from django.shortcuts import render, get_object_or_404, redirect
from .models import AddStock
from .forms import AddStockRegister
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def viewHome(request):

    stock = AddStock.objects.all()
    return render(request, "home.html", {"stock":stock})

def viewRead(request, id):

    stock = AddStock.objects.all()
    WantedStock = get_object_or_404(AddStock, pk=id)
    return render(request, "read.html",{"ResearchedStock":WantedStock, "id":id})

@login_required(login_url='/login-user')
def viewDelete(request, id):

    DeletedStock = get_object_or_404(AddStock, pk=id)
    DeletedStock.delete()
    return redirect('home')

@login_required(login_url='/login-user')
def viewCreate(request):

    formulario = AddStockRegister (request.POST, request.FILES,)
    if formulario.is_valid():
        formulario.save()
        return redirect('home')
    return render(request, 'create.html', {"formulario": formulario})

@login_required(login_url='/login-user')
def viewUpdate(request, id):

    ChangedStock = get_object_or_404(AddStock, pk=id)
    formulario = AddStockRegister (request.POST or None, instance=ChangedStock)
    if formulario.is_valid():
        formulario.save()
        return redirect('home')
    return render(request, "update.html", {'formulario': formulario})

def viewRegister(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'register.html', {'form_usuario': form_usuario})

def viewLoginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def viewLogout(request):
    logout(request)
    return redirect('home')

def viewChangePass(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'changePassword.html', {'form_senha': form_senha})
