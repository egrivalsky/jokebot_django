from django.shortcuts import render
from pynytimes import NYTAPI


# SECRET 2 GOES HERE

# Create your views here.

def index(request):
    return render(request, 'index.html')

def news(request):
    most_viewed = nyt.most_viewed(days = 7)
    for story in most_viewed:
        headline = story[title]
        url: story[url]
    list = {
        'headline': headline,
        'url': url
    }
    print(list)
    return render(request, 'news.html')

def about(request):
    return render(request, 'about.html')

