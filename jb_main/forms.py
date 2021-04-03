from django import forms
from .models import Profile, Joke

class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'about_me', 'twitter_handle', 'twitter_password']

