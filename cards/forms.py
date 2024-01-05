from django import forms

from .models import Calendar, Card 

class CalendarForm(forms.ModelForm):
    class Meta: 
        model = Calendar
        fields = ('name','available_from')

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('calendar', 'name', 'text', 'available_from')
        widgets = {
            'available_from' : forms.TextInput(attrs={'type':'datetime-local'}),
        }