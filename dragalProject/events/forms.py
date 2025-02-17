from django import forms 
from .models import Event, Game

class EventForm(forms.ModelForm):
    class Meta: 
        model =  Event
        fields = '__all__'
        exclude = ['slug']
        labels= { 
                 'title':'Title of Event',
                 'city':'City hosting the event',
                 'description':'Description of the Event',
                 'date':'Date of the event',
                 'logo':'Logo of the event',
                 'participants':'Participants of the event',
                 'games':'Games of the event'}
        error_messages = {}