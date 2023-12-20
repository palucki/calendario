from django import forms

from .models import Calendar, Card 

class CalendarForm(forms.ModelForm):
    class Meta: 
        model = Calendar
        fields = ('name',)

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('calendar', 'name', 'text', 'available_at')
        widgets = {
            'available_at' : forms.TextInput(attrs={'type':'datetime-local'}),
        }