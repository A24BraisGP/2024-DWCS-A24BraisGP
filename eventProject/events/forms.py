from django import forms 
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['slug']
        labels = {
            'title':'Title of the event',
            'city':'City hosting the event',
            'date':'date of the event',
            'ticket_price':'Price of the ticket',
            'artist':'Artist performing in the event',
            'description':'Description of the event',
            'logo':'Logo of the event'
        }
        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }
