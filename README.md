wikigame
========
There is a popular online game called Wiki Game (http://en.wikipedia.org/wiki/Wikipedia:Wiki_Game). The aim of the game is to get from a random Wikipedia page to another random Wikipedia page with as few steps as possible- the person with the least step wins. 

This Python script helps you always win the game ( I, in no way whatsoever, condone any form of cheating though. ;) ). It performs a bread-first search to give you the shortest path between any two Wikipedia pages (provided a path exists).

Usage
-----
- You will have to download the Wikipedia dump from http://dumps.wikimedia.org/ and run the script on the local dump because, obviously, Wikipedia puts a restriction on the number of requests you can send in a certain period of time. However, if you just want to try a demo, running the script as it is should work because the example pages in the script have a short path between them. 
- On line 77, put the URL of whatever page you want to begin with as the value of the variable 'start'.Then, put the URL of your goal page as the value of the variable 'goal' on line 78.
