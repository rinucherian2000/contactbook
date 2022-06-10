from django.forms import ModelForm
from book.models import Phone
from django import forms



class Phoneform(ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            # "date": forms.NumberInput(attrs={"class": "form-control"}),

        }