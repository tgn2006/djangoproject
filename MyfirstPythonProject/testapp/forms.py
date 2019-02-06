from django import forms
from django.contrib.auth.models import User
from testapp.models import Membership


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password','email','first_name', 'last_name']

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'
