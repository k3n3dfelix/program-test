from django.shortcuts import render, HttpResponseRedirect
from promotores.forms import PromotorForm
from promotores.forms import admForm, LoginForm
from django.contrib.auth import authenticate, logout, login as adm_login
from django.contrib.auth.decorators import login_required

def index(request):
	form = PromotorForm()	
	return render(request,'index.html',{'form':form})

def validar(request):
	if request.method =='POST':
		form = PromotorForm(request.POST)

		if form.is_valid():
			promotor = Promotor(**form.cleaned_data)
			promotor.save()

			promotores = Promotor.objects.all()

			return render(request,'validar.html',{'form':form,'promotores':promotores})
def login(request):ge
	form = LoginForm()
	return render(request,'login.html',{'form':form})

def validarlogin(request):
	if request.method =='POST':
		form - LoginForm(request.POST)

		if form.is_valid():
			adm = authenticate(username=form.data['login'], password=form.data['senha'])

			if adm is not None:
				if adm.is_active:
					meu_login(request,adm)
					return HttpResponseRedirect('/dashboard/')
				else:
					return render (request,'login.html',{'form':form})
			else:
				return render(request,'login.html',{'form':form})
		else:
			return render(request,'login.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')


def logoff(request):
	logout(request)
	return HttpResponseRedirect('/')
@login_required()
def dashboard(request):
	return render(request,'dashboard.html')