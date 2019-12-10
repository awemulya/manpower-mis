from .models import PassportInfo
from django import forms

class PassportForm(forms.ModelForm):
    class Meta:
        model = PassportInfo
        fields = "__all__"