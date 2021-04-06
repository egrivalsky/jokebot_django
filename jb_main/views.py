from django.shortcuts import render, redirect
from pynytimes import NYTAPI
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Joke, Profile, User
from .forms import JokeForm, ProfileForm
from django.contrib.auth.decorators import login_required
import twitter
from datetime import datetime, timedelta
from datamuse import datamuse
import time

datamuse=datamuse.Datamuse()

## SECRETS GO HERE *****************************************************************
twitter = twitter.Api(consumer_key='SKYECqSOCN6BMIbdcV1x7r5py',
                      consumer_secret='W8QAtdaYiJ9kLrrmA2SigFgxAJwwG1jid8VZm4Kky7l42qOJoC',
                      access_token_key='1376347053802975232-Rele3j0mkJ9PQrvtgazyRDru0G0UFm',
                      access_token_secret='1q6Mg8aXSEdH1wFninZSCpIlKIxLzMTfp2KdAtA2xFLGd')

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
    for n in response:
        n['adx_keywords'] = n['adx_keywords'].split(';')

    return render(request, 'news.html', { 
        'response': response, 
        })
@login_required
def news_keywords(request, story_id):
    response = nyt.most_viewed(days = 30)
    for n in response:
        if n['id'] == story_id:
            response = n
            n['adx_keywords'] = n['adx_keywords'].split(';')
    return render(request, 'keywords.html', { 
        'response': response, 
        })

def jokes(request):
    return render(request, 'jokes.html')

def about(request):
    return render(request, 'about.html')

# JOKES
def jokes_index(request):
    jokes = Joke.objects.filter(user = request.user).order_by('-id')
    return render(request, 'jokes/index.html', { 'jokes':jokes})

def joke_show(request, joke_id):
    joke = Joke.objects.get(id=joke_id)
    joke_form = JokeForm()
    last_tweeted = joke.last_tweeted
    print(f"Last Tweeted: {last_tweeted}")
    return render(request, 'jokes/show.html', {
        'joke':joke,
        'joke_form': joke_form,
    })


# CREATE VIEWS FOR FORMS
# class JokeCreate(CreateView):
#     model = Joke
#     fields = ['text', 'source', 'author']
#     success_url = '/jokes'

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

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['about_me', 'twitter_handle']
    success_url = '/profile'

def jokes_new(request):
    joke_form = JokeForm(request.POST)

    if  request.POST and joke_form.is_valid():
        new_joke = joke_form.save(commit=False)
        new_joke.user = request.user
        new_joke.save()

        return redirect('jokes')
    else:
        return render(request, 'jokes/new.html', { 'joke_form': joke_form })

# FUNCTIONS
@login_required
def joke_tweet(request, joke_id):
        joke = Joke.objects.get(id=joke_id)
        now = datetime.now()
        joke.last_tweeted = now
        message = joke.text
        twitter.PostUpdate(f"{message}")
        print(f"{message} last tweeted at {joke.last_tweeted}")
        time.sleep(5)
        return render(request, 'jokes/show.html', {
        'joke': joke,
        })

@login_required
def joke_favorite(request, joke_id):
    joke = Joke.objects.get(id=joke_id).order_by('-id')
    user = request.user
    user.profile.favorites.add(joke)
    return render(request, 'jokes/show.html', {
    'joke':joke,
    })

@login_required
def related_words(request, word):
    related = datamuse.words(rel_jja=word)
    rhymes = datamuse.words(rel_rhy=word)
    print(word)
    word_list = []
    for n in related:
        related_words = n['word']
        word_list.append(related_words)
    for n in rhymes:
        related_words = n['word']
        word_list.append(related_words)
    return render(request, 'related_words.html', {'word_list': word_list})


# PROFILE
def profile(request):
    user = request.user
    user_id=user.id
    fav_jokes = user.profile.favorites.all()
    written_jokes = Joke.objects.filter(user=user_id)
    return render(request, 'profile.html', {
        'user': user,
        'fav_jokes': fav_jokes,
        'written_jokes': written_jokes
    })



