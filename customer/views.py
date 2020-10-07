from django.http import Http404
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm, ProdForm, CartForm, OrderForm
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
		if request.method == 'POST':	
			if 'custom' in request.POST:
				return render(request,'warehouse/registration.html')
			elif 'produkto' in request.POST:
				return redirect('customer:prodreg_view')
			elif 'Browse' in request.POST:
				return redirect('customer:products_view')


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


class ProductView(View):
	def get(self,request):
		qs_products = Product.objects.all()
		qs_cart = Cart.objects.all()
		context = {
			'products'	: qs_products,
			'cart'      : qs_cart
		}
		return render(request,'warehouse/Products.html',context)

	def post(self,request):
		cform = OrderForm(request.POST,request.FILES)
		if request.method == 'POST':
			if 'addtocart' in request.POST:
				if cform.is_valid():
					namaewa = request.POST.get("product-name")
					proice = request.POST.get("product-proice")
					amount = request.POST.get("quantity")
					cform = Order(name=namaewa,price=proice,quantity = amount)
					cform.save()
					return redirect('customer:products_view')
				else:
					print(cform.errors)
					return HttpResponse('Invalid data')
			elif 'gotocart' in request.POST:
				return redirect('customer:cart_view')
			elif 'gohome' in request.POST:
				return redirect('customer:landing_view')


class CartView(View):
	def get(self,request):
		qs_products = Product.objects.all()
		qs_cart = Cart.objects.all()
		qs_order = Order.objects.all()
		context = {
			'products'	: qs_products,
			'cart'      : qs_cart,
			'orders'		: qs_order
		}
		return render(request,'warehouse/cart.html',context)

	def post(self,request):
		
		if request.method == 'POST':	
			if 'conpirmOrder' in request.POST:
				itemID = request.POST.get("items-id")
				#itemname = request.POST.get("items-name")
				#itemprice = request.POST.get("items-price")
				itemquantity = request.POST.get("items-quantity")
				orderDate = request.POST.get("orderdate")
				orderLocation = request.POST.get("location")
				final = Order.objects.filter(cart_ptr_id = itemID).update(quantity =itemquantity,orderdate = orderDate, location = orderLocation)
				#form = Order( name=itemname,price=itemprice,quantity=itemquantity,cart_ptr_id=itemID, orderdate = orderDate, location = orderLocation)
				#form.save()
				print('order received')
			elif 'cancelOrder' in request.POST:
				orderID = request.POST.get("del-targetID")
				cusTard = Order.objects.filter(cart_ptr_id = orderID).delete()
				personbye = Cart.objects.filter(id = orderID).delete()
				print(orderID)
				print('Order is deleted')
		return redirect('customer:cart_view')
# def display_prod_pics(request): 
  
#     if request.method == 'GET': 
#         # getting all the objects of hotel. 
#         prod = Product.objects.all()  
#         return render((request, 'warehouse/dashboard.html', 
#                      {'prod_images' : prod})) 
