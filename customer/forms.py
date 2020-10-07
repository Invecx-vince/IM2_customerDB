from django import forms
from .models import *

class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ("name",)

class ProdForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ("name",)

class CartForm(forms.ModelForm):

	class Meta:
		model = Cart
		fields = ("quantity",)


class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ("quantity",)
