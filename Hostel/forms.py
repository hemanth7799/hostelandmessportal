from django import forms

from Hostel.models import RoomRegistration


class RoomRegistrationForm(forms.ModelForm):
    class Meta:
        model = RoomRegistration
	
	fields = ('pref_room_no', 'fee_proof', 'hostel_name',)
