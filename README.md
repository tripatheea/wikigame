wikigame
========
There is a popular online game called Wiki Game (http://en.wikipedia.org/wiki/Wikipedia:Wiki_Game). The aim of the game is to get from a random Wikipedia page to another random Wikipedia page with as few steps as possible- the person with the least step wins. 

This Python scripts is intended to help (help but NOT condone ;) ) a player to cheat. It performs a bread-first search to give you the shortest path between any two Wikipedia pages (provided a path exists).

Usage
-----
- You will have to download the Wikipedia dump from http://dumps.wikimedia.org/ and run the script on the local dump because, obviously, Wikipedia puts a restrictions to the number of requests you can send in a fixed period of time. However, if you just want to try a demo, running the script as it is should work because the example pages in the script have a small path between them. 
- On line 77 and 78 of the script, put the URL of whatever page you want to begin with as the value of the variable 'start'.Then, put the URL of your goal page as the value of the variable 'goal'.
