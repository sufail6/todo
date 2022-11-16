from django import forms

from app.models import Mod


class Card(forms.ModelForm):
    class Meta:
        model = Mod
        fields = '__all__'