# Nikhil's Personal Search Engine (Memex)
---
## Overview
This is my attempt at making a tool that will be able to pull in data from many different sources where I've left a digital footprint and aggregate them into a uniform index that I can search through.

## Progress
As of November, I've got a working MVP that does some basic functionality e.g. (1) I pass in a search term (2) it goes through a generated `index.json` file from my ~~Facebook~~ Meta Messenger history and then (3) spits out a list of all of the messages where the search term has been referenced.

INSERT VIDEO

This is great, but there's still a lot to do! Here's a non-exhaustive things that I hope to add to this in the coming months:
* more data sources
  * roam research graph
  * google takeout data
  * text messages
  * public content (tweets, blog posts)
  * twitter likes
  * read-it-later articles
* stemming to tokens to reduce repetiton
* a `react.js` UI to easily search
* *much more*

## Context
*pulled from my [blog post](https://nikhilthota.com/writing/memex/) on the topic*

Why is this even useful? The human brain isn’t designed to store the vast amounts of information that we create in our modern world. It can approximate this ability to some extent by surfacing thing in associative contexts (going from the word “gray” ⬜️ -> gray dog 🐩 -> your childhood dog sparky 🥺 -> a memory of the time he ate your homework 🧾). However, storing data isn’t what the brain is best at — it’s best at forming connections from information that it loads into working memory.

This is why I’m so obsessed with knowledge management and can spend hours sorting out my thoughts & learning into the right contexts. The closest thing I’ve come to having my own memex is my [Roam Research](https://roamresearch.com/) graph, but even that has its limitations. Everything I can find in my Roam is something that I’ve actively parsed through and taken the time to write down. **What about the vast amounts of memories, experiences, insight, and information that don’t get written down?**
