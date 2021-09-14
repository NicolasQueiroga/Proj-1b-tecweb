from django import forms
from .models import Note


class NoteCreate(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
