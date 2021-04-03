from django.shortcuts import render, redirect
from pynytimes import NYTAPI
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Joke, Profile, User
from .forms import JokeForm, ProfileForm
from django.contrib.auth.decorators import login_required
import json

nyt = NYTAPI('FtZ0xW7RIZ9wRxJJiR02MNv37ChQGZPO', parse_dates=True)

# Create your views here.
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def index(request):
    return render(request, 'index.html')

def news(request):
    response = nyt.most_viewed(days = 30)

    return render(request, 'news.html', { 'response': response })

def jokes(request):
    return render(request, 'jokes.html')

def about(request):
    return render(request, 'about.html')

# JOKES
def jokes_index(request):
    jokes = Joke.objects.filter(user = request.user)
    return render(request, 'jokes/index.html', { 'jokes':jokes})

def joke_show(request, joke_id):
    joke = Joke.objects.get(id=joke_id)
    joke_form = JokeForm()
    return render(request, 'jokes/show.html', {
        'joke':joke,
        'joke_form': joke_form
    })




# CREATE VIEWS FOR FORMS
class JokeCreate(CreateView):
    model = Joke
    fields = ['text', 'source', 'author']
    success_url = '/jokes'

class JokeUpdate(UpdateView):
    model = Joke
    fields = ['text', 'author', 'source']

def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/jokes/' + str(self.object.pk))

class JokeDelete(DeleteView):
    model = Joke
    success_url = '/jokes'

@login_required()
def jokes_new(request):
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
    joke_form = JokeForm(request.POST)

    if  request.POST and joke_form.is_valid():
        new_joke = joke_form.save(commit=False)
        new_joke.user = request.user
        new_joke.save()

        return redirect('jokes')
    else:
        print('****************************************************')
        return render(request, 'jokes/new.html', { 'joke_form': joke_form })

