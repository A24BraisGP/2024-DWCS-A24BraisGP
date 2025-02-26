from django import forms 
from .models import Event, Artist

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['slug']
        labels = {
            'title':'Title of the event',
            'city':'City hosting the event',
            'date':'Date of the event',
            'ticket_price':'Price of the ticket',
            'artist':'Artist performing in the event',
            'description':'Description of the event',
            'logo':'Logo of the event'
        }
        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

class ArtistForm(forms.ModelForm):
    
    class Meta: 
        model = Artist
        fields = '__all__'
        labels ={
            'name': 'Name of the artist',
            'genre': 'Genre of music of the artist',
            'picture':'Flatering picture of the artist',
            'songs':'List of songs the artist is performing (SEPARATED BY COMMA)'
        }