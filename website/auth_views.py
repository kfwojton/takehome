
from django.views.generic import *
from core.models import *
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from django.views.generic import FormView
from core.models import Profile
from django.contrib.auth import login, logout 
from django.shortcuts import redirect
from website.forms import RegistrationForm




from website.settings import DEBUG

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def get_context_data(self, **kwargs):

        context = super(Login, self).get_context_data(**kwargs)
        context['registration_form'] = RegistrationForm

        return context

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            print('is valid')
            user = form.get_user()
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            print('is not valid')
            return self.form_invalid(form)

class Logout(FormView):

    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect("/")



class SignUp(FormView):
    form_class = RegistrationForm
    success_url = "/"
    template_name = "login.html"

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            #create user if doesn't exist.
            try:
                user = User.objects.create(
                email = self.request.POST["username"],
                username = self.request.POST["username"],
                first_name = self.request.POST["first_name"],
                last_name = self.request.POST["last_name"])
            except Exception as e:

                form.add_error(None, str(e))  
                print(e)
                # tell user username is already taken
                messages.add_message(request, messages.WARNING, e)
                return redirect('/signup/' )


            user.save()

            login(self.request, user)
            user = self.request.user
            # create profile, instead of extending user model for more flexilibity. The profile is a one-to-one relationship with the user.
            Profile.objects.create(user = user )

            profile = self.request.user.profile

            # Todo: Usually I like to initial stripe customer information on sign up. I would add this later. 
            # profile.stripe_customer_id = stripe.Customer.create().id
        
            profile.save()
          
            # Todo: I would send them a welcome email here. 
            # send_email(self.request.profile.user.username, '....')
        
            return redirect(self.get_success_url())
        else:

            return self.form_invalid(form)



