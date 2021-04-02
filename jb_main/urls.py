from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('about', views.about, name='about'),
    path('jokes', views.jokes, name='jokes'),
    path('accounts/signup', views.signup, name="signup"),
    path('jokes/create/', views.JokeCreate.as_view(), name='jokes_create'),
    path('jokes/<int:pk>/update/', views.JokeUpdate.as_view(), name='jokes_update'),
    path('jokes/<int:pk>/delete/', views.JokeDelete.as_view(), name='jokes_delete')
]