from .models import PassportInfo
from django import forms
from django.forms.fields import DateField
class PassportForm(forms.ModelForm):
    entry_date = forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model = PassportInfo
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Full Name'}),
            'passport_no':forms.TextInput(attrs={'placeholder':'Passport Number', 'type':'number'}),
            'reference':forms.TextInput(attrs={'placeholder':'Reference Through'}),
        }