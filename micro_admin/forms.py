from django import forms
from django.forms import ModelForm
from micro_admin.models import Branch, Client

class BranchForm(forms.ModelForm):

    class Meta:
        model = Branch
        fields = ['name', 'opening_date', 'country', 'state', 'district', 'city', 'area', 'phone_number', 'pincode']


class EditbranchForm(forms.ModelForm):

    class Meta:
        model = Branch
        fields = ['country', 'state', 'district', 'city', 'area', 'phone_number', 'pincode']


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ["email", "mobile", "pincode", "photo", "signature", "blood_group"]