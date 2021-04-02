# JokeBot
Jokebot is currently under development tweeting from @jokebot_dev

## Overview
Jokebot uses current event APIs, keyword extraction, and joke databases share topical humor

Make sure you review your project proposal with your instructor so you can make sure it's **something you can accomplish in the limited time we have**, and make sure it's **something that'll showcase your skills both visually and functionally**. Sometimes people do judge a book by its cover – or in this case, an app by its design.

## Technical Requirements

The app will:

* **Use Django to build an application backend 
* **Use React and/or Django Templates to build out the front-end
* **Will use at least 2 related models, one of which should be a user

## At a minimum:
* **Have user authentication
* **Search for and often find a joke based on a keyword
* **Let user save the joke to their list of jokes
* **Let user delete/edit jokes from their list of jokes

## Hopefully:
* **Tweet out jokes from @JokeBot
* **Allow other users to tweet the jokes JokeBot finds for them

## General approach for MVC:
  Use NY Times API to find most popular articles, use python subject extraction to find what the keywords to the articles are. 
  Use one of those keywords to search one free joke API or database. Then the user, if logged in, can save that joke to their list of jokes. The ser
  will also have the opportunity to annotate or delete the joke.
  
  Once that works I will expand the number of news sources, number of joke sources, and allow the user to add their twitter account to they can tweet
  the joke returned directly from the web app.
  
 ## User Stories
  * As a user I want to see current events when I log in
  * As a user I want to search for jokes based on current events
  * As a user, I'd like to save a returned joke to my favorites list
  * As a user, I'd like to be able to add a note to a joke
  * As a user, I'd like to delete a joke (and my note, if any) from my favorites list
  * As a user, I'd like to write a joke and save it to my favorites list
  
 ## ERD
 (![ERD](https://user-images.githubusercontent.com/72841900/112911379-88e1a600-90b2-11eb-950c-767f39b1c31f.png))

