from django import forms
from customers.models import Customer

class CustomerForm(forms.Form):
    name = forms.CharField(required=True, max_length=20,label='NAME:')
    email = forms.EmailField(required=True, label='EMAIL:',min_length=10, max_length=30)
    phone = forms.IntegerField(required=True, label='PHONE:',)
    address = forms.CharField(required=True, label='ADDRESS:')

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name:'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter your email:'}),
            'gender': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your gender:'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter your age:'}),
        }