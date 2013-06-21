from django import forms
from django.forms import extras
from datetime import date 

class SelectForm(forms.Form):
    check_in = forms.DateField(widget=extras.widgets.SelectDateWidget, initial=date.today)
    check_out = forms.DateField(widget=extras.widgets.SelectDateWidget, initial=date.today)
