from django import forms

from testapi.models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields="__all__"
        widgets={

            "name":forms.TextInput(attrs={"class":"form-control"}),
            "date": forms.DateInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "income": forms.NumberInput(attrs={"class": "form-control"}),
            "ipaddress":forms.TextInput(attrs={"class": "form-control"})


        }