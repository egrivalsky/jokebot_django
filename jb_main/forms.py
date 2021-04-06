from django import forms
from .models import Profile, Joke

class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = ['text', 'source', 'author']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

