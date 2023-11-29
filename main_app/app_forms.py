from django import forms

from main_app.models import Donors


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = "__all__"
        ORGANIZATION_CHOICES = ["KNH", "Nairobi South", "Nairobi West"]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date", "min": "1990-01-01", "max": "2005-12-31"}),
            "organization": forms.Select(attrs={"organization": ORGANIZATION_CHOICES}),
        }
        labels = {
            "dob": "Date of Birth",
            "email": "Email Address",
            "organization": "Organization",
            "bloodgroup": "Blood Group",
            "location": "Location",
            "name": "Full Name",
        }
