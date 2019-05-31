from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['writer']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','bio','contact']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name','location','count']
