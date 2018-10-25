from __future__ import unicode_literals
from django.db import models
#from hostel.models import Student
class MessFeedback(models.Model):
	roll_no= models.ForeignKey(Student,on_delete=models.CASCADE)
	feedbackid = models.CharField(max_length=250)
	time = models.CharField(max_length=250)
	feedback = models.CharField(max_length=200)
	def __str__(self):
		return str(str(self.feedback) +","+str(self.time))
class Refund(models.Model):
	roll_no= models.ForeignKey(Student,on_delete=models.CASCADE)
	#employeeid= ForeignKey(Employee,on_delete=models.CASCADE)
	refundid = models.CharField(max_length=250)
	outdate=models.CharField(max_length=200)
	indate=models.CharField(max_length=200)

	def __str__(self):
		return str(self.outdate+","+self.indate)
