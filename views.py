from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm
from .models import *

# Create your views here.
class BoardView(View):
	def get(self,request):
		return render(request,'warehouse/dashboard.html')

	def post(self,request):
		return render(request,'warehouse/registration.html')


class RegisterView(View):
	def get(self,request):
		return render(request,'warehouse/registration.html')

	def post(self,request):	
		form = CustomerForm(request.POST)
		#namaewa = request.POST.get("fullname")
		#print(form.name)
		#adres = request.POST.get("addressu")
		#print(adres)
		if form.is_valid():
			
			namaewa = request.POST.get("name")
			adres = request.POST.get("address")
			bday = request.POST.get("birday")
			tatus = request.POST.get("statusu")
			sex = request.POST.get("genderu")
			
			form = Customer( name = namaewa , address = adres , birthdate = bday , status = tatus , gender = sex )
			form.save()

			return HttpResponse('Customer Recorded!!!')

		else:
			print(form.errors)
			return HttpResponse('Invalid data')




class LandingView(View):
	def get(self,request):
		return render(request,'warehouse/NeoSGP_home.html')

	def post(self,request):
		return render(request,'warehouse/registration.html')

