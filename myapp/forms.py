from django import forms
from . models import Image
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
        labels = {'photo': ""}

