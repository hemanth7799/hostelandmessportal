from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RefundForm,FeedbackForm
from django.contrib.auth import get_user_model
from Hostel.models  import Student
from .models import *
User = get_user_model()

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg','pdf']


def refund(request):
    if not request.user.is_authenticated():
        return render(request, 'Mess/login.html')
    else:
        form = RefundForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            mess = form.save(commit=False)
            mess.student = Student.objects.get(user=request.user)
            mess.mail_proof = request.FILES['mail_proof']
            file_type = mess.mail_proof.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'mess': mess,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'Mess/refund.html', context)
            mess.save()
            return HttpResponse("Advance happy diwali")
        context = {
            "form": form,
        }
        return render(request, 'Mess/refund.html', context)
def feedback(request):
    if not request.user.is_authenticated():
        return render(request, 'Mess/login.html')
    else:
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            mess = form.save(commit=False)
            mess.student = Student.objects.get(user=request.user)
            mess.save()
            return render(request, 'Mess/feedbacksuccess.html', {'error_message': 'feedback submitted successfully'})
        context = {
            "form": form
        }
        return render(request, 'Mess/feedback.html', context)
def feedbacklist(request):
    if  request.user.is_authenticated():
	mess=MessFeedback.objects.all()
        return render(request, 'Mess/feedbacklist.html', {'mess':mess})
    else:
	return HttpResponse("Login as employee")
def refundlist(request):
    if not request.user.is_authenticated():
        return render(request, 'Mess/login.html')
    else:
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            mess = form.save(commit=False)
            mess.student = Student.objects.get(user=request.user)
            mess.save()
            return render(request, 'Mess/feedback.html', {'error_message': 'feedback submitted successfully'})
        context = {
            "form": form
        }
        return render(request, 'Mess/feedback.html', context)

import json
import requests
from django.shortcuts import get_object_or_404, render

def login(request,token):
    print ('hello')
    res = requests.post(url='https://serene-wildwood-35121.herokuapp.com/oauth/getDetails', data={
    'token': token,
    'secret': 'ff5bbfae032e66f2abdb15b113bfab5d3f1741b1ed1f60b04e7062d74024bad29f57b82e6cfe0eee53ee6e595405c00907af0179c85c2c0c396e6e3df1f250a7'
})
    res = json.loads(res.content)
    email = res['student'][0]['Student_Email']
    print(email)
    if(email):
        return render(request,'Mess/login.html')






