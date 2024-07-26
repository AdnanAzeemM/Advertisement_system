from django import forms
from .models import Location, Ad, Advertisement


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = '__all__'
