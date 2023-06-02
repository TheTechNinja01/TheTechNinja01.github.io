from django.forms import ModelForm
from django import forms
from .models import tickets_notifications

class UserLogIn(ModelForm):
    pass

class TicketUpload(ModelForm):
    Subject = forms.TextInput()
    Message = forms.TextInput()
    ticket_or_notification = forms.TextInput()

    class Meta:
        model = tickets_notifications
        fields  = ['Subject', 'Message', 'ticket_or_notification']


