from django import forms
from ecommerce.utils import verify_email
"""Here all the forms used to verify data is OK"""


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    def is_valid(self) -> bool:
        is_valid = super().is_valid()
        for key, val in self.cleaned_data.items():
            print(key, val)
            if val == None:
                return False
        return is_valid

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if verify_email(email):
            return email
        else:
            return None

    def clean_password(self):
        return self.cleaned_data.get("password")


class GuestEmailForm(forms.Form):
    email = forms.CharField(max_length=50)
