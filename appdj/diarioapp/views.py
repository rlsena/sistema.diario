from django.shortcuts import render, redirect, get_object_or_404
from .forms import Loginform
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .models import Diario
from django.contrib.auth.decorators import login_required
from .forms import DiarioForm
# Create your views here.
def excluir_diario(request,id):
    diario=get_object_or_404(Diario,id=id)
    diario.delete()
    return redirect('index')

def editar_diario(request,id):
    diario=get_object_or_404(Diario,id=id)
    form=DiarioForm(instance=diario)
    if request.POST:
        form=DiarioForm(request.POST,instance=diario)
        if form.is_valid():
            form.user=request.user
            form.save()
            return redirect('index')
    context={
        'form':form,
    }
    return render (request, 'diario/editar.html', context)

def escrever_diario(request):
    if request.POST:
        form=DiarioForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('index')
    
    
    form=DiarioForm()
    context={
        'form':form,
    }
    return render (request, 'diario/escrever.html', context)

def fazer_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    diario=Diario.objects.filter(user=request.user)
    context={
        'diario':diario,
    }
    return render(request,'diario/index.html', context)

   

def fazer_login(request):
    if request.POST:
        form=Loginform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('<h1> Usuário ou senha invalidos! </h1>')

    form=Loginform()
    context={
        'form':form,
    }
    return render(request,'diario/login.html', context)