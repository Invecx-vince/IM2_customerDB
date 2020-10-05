from django.http import Http404
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm, ProdForm
from .models import *

# Create your views here.
class BoardView(View):
	def get(self,request):
		qs_customers = Customer.objects.all()
		qs_products = Product.objects.all()
		context = {
			'customers' : qs_customers,
			'products'	: qs_products
		}

		return render(request,'warehouse/dashboard.html',context)

	def post(self,request):
		# return render(request,'warehouse/registration.html')
		if request.method == 'POST':	
			if 'btnUpdate' in request.POST:
				custID = request.POST.get("customer-id")
				namaewa = request.POST.get("customer-name")
				adres = request.POST.get("customer-address")
				bday = request.POST.get("customer-bdate")
				tatus = request.POST.get("customer-status")
				sex = request.POST.get("customer-gender")
				up_cstmr = Customer.objects.filter(person_ptr_id = custID).update(name = namaewa , address = adres , birthdate = bday , status = tatus , gender = sex)
				print(up_cstmr)
				print('record updated')
			elif 'btnDelete' in request.POST:
				custID = request.POST.get("del-targetID")
				cusTard = Customer.objects.filter(person_ptr_id = custID).delete()
				personbye = Person.objects.filter(id = custID).delete()
				print(custID)
				print('record with said custID is deleted')
		return redirect('customer:board_view')

		

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

			# return HttpResponse('Customer Recorded!!!')
			return redirect('customer:board_view')
			# render(request,'warehouse/dashboard.html')

		else:
			print(form.errors)
			return HttpResponse('Invalid data')



class LandingView(View):
	def get(self,request):
		return render(request,'warehouse/NeoSGP_home.html')

	def post(self,request):
		return render(request,'warehouse/registration.html')


class ProdRegView(View):
	def get(self,request):
		return render(request,'warehouse/prodregis.html')

	def post(self,request):	
		form = ProdForm(request.POST,request.FILES)
		#namaewa = request.POST.get("fullname")
		#print(form.name)
		#adres = request.POST.get("addressu")
		#print(adres)
		if form.is_valid():
			
			namaewa = request.POST.get("name")
			value = request.POST.get("p_price")
			pic = request.FILES.get("prodPic")
			if(request.POST.get("p_isDoz")=="Yes"):
				doz=True
			else:
				doz=False
			form = Product( name = namaewa , price=value, picture = pic, byDozen = doz)
			form.save()

			# return HttpResponse('Customer Recorded!!!')
			return redirect('customer:board_view')
			# render(request,'warehouse/dashboard.html')

		else:
			print(form.errors)
			return HttpResponse('Invalid data')

# def display_prod_pics(request): 
  
#     if request.method == 'GET': 
#         # getting all the objects of hotel. 
#         prod = Product.objects.all()  
#         return render((request, 'warehouse/dashboard.html', 
#                      {'prod_images' : prod})) 
