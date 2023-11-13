from django import forms
from .models import Person
class EditPost(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name','address','profile_pic']
        labels={'name':'Name','address':'Address','profile_pic':'Profile_Pic'}