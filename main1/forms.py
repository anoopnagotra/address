from django.forms import ModelForm
from main.models import Event, Ticket
from bootstrap_datepicker_plus import DateTimePickerInput


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_start', 'event_end']
        widgets = {
            'event_start': DateTimePickerInput(),
            'event_end': DateTimePickerInput()
        }


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_name', 'event_id']
