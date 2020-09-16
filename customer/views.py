from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class BoardView(View):
	def get(self,request):
		return render(request,'warehouse/dashboard.html')

	def post(self,request):
		return render(request,'warehouse/registration.html')


class RegisterView(View):
	def get(self,request):
		return render(request,'warehouse/registration.html')

class LandingView(View):
	def get(self,request):
		return render(request,'warehouse/NeoSGP_home.html')

	def post(self,request):
		return render(request,'warehouse/registration.html')

