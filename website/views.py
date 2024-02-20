
from django.views.generic import *
from core.models import *
from website.forms import InvestorForm, AllocationForm
from core.models import *
from django.contrib.auth.models import User

from website.functions import transform_to_allocation_input
from django.shortcuts import render

def about_us_view(request):
    return render(request, 'about_us.html') 


def allocation_view(request):
    context = {}
    context['allocation_form'] =  AllocationForm()
    context['investor_form'] = InvestorForm()
#
        
    if request.method == 'POST':
        
       
        form = AllocationForm(request.POST)
        # form = MyForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            
            context['data'] = transform_to_allocation_input(request.POST, request.user)
            return render(request, 'allocation.html', {'context': context } )
        else:
            # Form is invalid, handle errors
            context['errors'] = form.errors
        
            return render(request, 'allocation.html',  {'context': context })
    else:
        # If it's a GET request or any other method, create a blank form
       
        return render(request, 'allocation.html', {'context': context })