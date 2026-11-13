from django import forms

from Myapp.models import Books

# django forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','category','year','isbn','cost','cover','published']