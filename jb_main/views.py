from django.shortcuts import render
from pynytimes import NYTAPI
from joke.jokes import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import *

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
    return HttpResponseRedirect('/cats/' + str(self.object.pk))

class JokeDelete(DeleteView):
    model = Joke
    success_url = '/jokes'

def jokes_new(request):
    joke_form = JokeForm(request.POST or None)

    if request.POST and joke_form.is_valid():
        new_joke = joke_form.save(commit=False)
        new_joke.user = request.user
        new_joke.save()
        return redirect('jokes')
    else:
        return render(request, 'jokes/new.html', { 'joke_form': joke_form })

