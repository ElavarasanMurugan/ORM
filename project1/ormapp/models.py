from django.db import models
from django.contrib import admin
class Loan(models.Model):
	Name=models.CharField(max_length=20)
	AccountNumber=models.IntegerField(primary_key=True)
	IFSCcode=models.CharField(max_length=11)
	LoanAmount=models.DecimalField(max_digits=10,decimal_places=2)
class LoanAdmin(admin.ModelAdmin):
		list_display=('Name','AccountNumber','IFSCcode','LoanAmount')