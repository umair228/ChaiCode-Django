from django import forms
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(),label='Chai Varity')


