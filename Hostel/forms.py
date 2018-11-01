
from django import forms
from django.contrib.auth.models import User

from Hostel.models import RoomRegistration


class RoomRegistrationForm(forms.ModelForm):
	
	class Meta:
		model = RoomRegistration
		student = forms.CharField()
		fields = ('pref_room_no', 'fee_proof','hostel_name' ,)
from django.forms import ModelForm

class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["email", "password"]


