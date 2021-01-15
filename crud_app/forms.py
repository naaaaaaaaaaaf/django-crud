from django import forms
class BmiForm(forms.Form):
    height = forms.FloatField(label='身長(cm)',
    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight = forms.FloatField(label='体重(kg)',
    widget=forms.NumberInput(attrs={'class': 'form-control'}))
