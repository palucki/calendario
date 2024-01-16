from django import forms
from django.forms.models import inlineformset_factory
from ckeditor.widgets import CKEditorWidget

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
            'text' : CKEditorWidget()
        }

CardFormSet = inlineformset_factory(
    Calendar, 
    Card,
    form = CardForm,
    min_num = 1,
    can_delete=False,
    extra = 0 #see what it does
)