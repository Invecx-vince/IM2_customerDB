from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 50)
	birthdate = models.DateField()
	
	
	gender = models.CharField(max_length = 6)
	
	class Meta: #optional for not getting default table name which is projectname_ClassName
		db_table = "Person"

class Customer(Person):
	status = models.CharField(max_length = 10)
	#email = models.EmailField()
	#phone = models.CharField(max_length = 11)

	class Meta: #optional for not getting default table name which is projectname_ClassName
		db_table = "Customer"

class Product(models.Model):
	#email = models.EmailField(default = '', null = False)
	name = models.CharField(max_length = 100)
	price = models.IntegerField()
	picture = models.ImageField(upload_to='prodImages',blank = True, null = True)
	byDozen = models.BooleanField()
	
	class Meta: #optional for not getting default table name which is projectname_ClassName
		db_table = "Product"
