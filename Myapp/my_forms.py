from typing import Any

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Myapp.models import Books

# django forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','category','year','isbn','cost','cover','published']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control rounded - 0'


    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']