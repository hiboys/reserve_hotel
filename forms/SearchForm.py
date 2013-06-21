from django import forms
from django.forms import extras
from datetime import date 
class SearchForm(forms.Form):
    city = forms.CharField() 
    check_in = forms.DateField(widget=extras.widgets.SelectDateWidget, initial=date.today)
    check_out = forms.DateField(widget=extras.widgets.SelectDateWidget, initial=date.today)
