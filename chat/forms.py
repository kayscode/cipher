from django import forms
from .models import User


# user form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "avatar"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': "form-input"}),
            "last_name": forms.TextInput(attrs={'class': "form-input"}),
            "email": forms.EmailInput(attrs={'class': "form-input"}),
            "password": forms.PasswordInput(attrs={'class': "form-input"}),
            "avatar": forms.FileInput(attrs={'class': "form-input",'required':None}),
        }


# messaging form
class MessageForm(forms.Form):
    sender = forms.IntegerField(widget=forms.NumberInput(
        attrs={}
    ))
    receiver = forms.IntegerField(widget=forms.NumberInput(
        attrs={}
    ))
    text = forms.CharField(widget=forms.Textarea(
        attrs={}
    ))

    cipher_key = forms.CharField(widget=forms.TextInput(
        attrs={}
    ))
