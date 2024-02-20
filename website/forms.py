from website.functions import *
from django import forms
from django.views.generic import FormView
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class InvestorForm(forms.Form):
    investor_name = forms.CharField()
    requested_amount =  forms.IntegerField(label='Target Invested Amount:')
    average_amount =  forms.IntegerField(label='Amount Previous Invested:')

class AllocationForm(forms.Form):
    allocation_amount = forms.IntegerField(label='Total Fundraise Target:')
 
class RegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("email","first_name", "last_name", "password1", "password2")


