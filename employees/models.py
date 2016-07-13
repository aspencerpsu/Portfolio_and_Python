from django.db import models

class Employee(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	address=models.CharField(max_length=50)

	hire_date=models.DateField()
	email=models.EmailField()

# Create your models here.

class Employer(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	hire_date=models.DateField()
	email=models.EmailField()

