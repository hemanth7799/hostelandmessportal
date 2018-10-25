from __future__ import unicode_literals
from django.db import models
from Hostel.models import Student
class MessFeedback(models.Model):
	student= models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	feedbackid = models.CharField(max_length=250)
	time = models.CharField(max_length=250)
	feedback = models.CharField(max_length=200)
	def __str__(self):
		return str(str(self.feedback) +","+str(self.time))
class Refund(models.Model):
	student= models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	#employeeid= ForeignKey(Employee,on_delete=models.CASCADE)
	refundid = models.CharField(max_length=250)
	outdate=models.CharField(max_length=200)
	indate=models.CharField(max_length=200)
	mail_proof=models.FileField(default=None)

	def __str__(self):
		return str(self.outdate+","+self.indate)
class BankDetails(models.Model):
	student   = models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	bank_name =models.CharField(max_length=250)
	ifsc      =models.CharField(max_length=250)
        branchname =models.CharField(max_length=250)
	acholdername=models.CharField(max_length=250)
