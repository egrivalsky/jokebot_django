from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('about', views.about, name='about'),
    # path('jokes', views.jokes, name='jokes'),
    path('accounts/signup', views.signup, name="signup"),
    path('jokes', views.jokes_index, name='jokes'),
    path('jokes/create/', views.jokes_new, name='jokes_create'),
    path('jokes/<int:joke_id>/', views.joke_show, name='joke_show'),
    path('jokes/<int:joke_id>/joke_tweet', views.joke_tweet, name='joke_tweet'),
    path('jokes/<int:joke_id>/joke_favorite', views.joke_favorite, name='joke_favorite'),
    path('jokes/<int:pk>/update/', views.JokeUpdate.as_view(), name='jokes_update'),
    path('jokes/<int:pk>/delete/', views.JokeDelete.as_view(), name='jokes_delete'),
    path('profile', views.profile, name='profile')
]