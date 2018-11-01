from django import forms
from django.contrib.auth.models import User

from .models import Refund,MessFeedback


class RefundForm(forms.ModelForm):

    class Meta:
        model = Refund
        fields = ['from_date', 'to_date', 'mail_proof']
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = MessFeedback
        fields = ['feedback']

