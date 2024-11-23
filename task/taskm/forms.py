from django import forms
from .models import Task, SendInvitation

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

class SendInvitationForm(forms.ModelForm):
    class Meta:
        model = SendInvitation
        fields = ['email']