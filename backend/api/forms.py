from django import forms
from .models import Email

class EmailForm(forms.Form):
    template = forms.ModelChoiceField(queryset=Email.objects.all(), required=True)
    include_qr = forms.BooleanField(required=False, label="Include QR Code")