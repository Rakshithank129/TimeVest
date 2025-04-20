from django import forms
from taskmanagement.models import tasks

class taskForm(forms.ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'

    