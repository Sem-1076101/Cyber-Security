from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class CreateEmployeeForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
            'firstName', 'lastName', 
            'email', 'password1', 
            'password2', 'gender', 
            'birhday', 'phone_number',
            'zipCode', 'home_number', 
            'admin']