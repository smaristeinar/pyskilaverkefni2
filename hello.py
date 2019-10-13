from easygui import *
from playsound import *
import pygame
import glob
import os


song = os.listdir("songs")
songs = []

for i in song:
    if i[-3:] == "mp3":
        songs.append(i)
currentsong = ""


msg = "song:"
image = "log.gif"
btns = ["play","paus", "quit","select song", "+","-"]

volume = 1

pygame.mixer.init()
while True:
    flag1 = buttonbox(msg ,choices = btns,image = image , title = "$GANGSTAMP3$")

    if flag1 == "play":
        pygame.mixer.music.unpause()
        print(pygame.mixer.music.get_volume())
    if flag1 == "paus":
        pygame.mixer.music.pause()
        print("music is now paused")
    if flag1 == "select song":
        selectedsong =choicebox("select a song","playlist",songs)
        pygame.mixer.music.load("songs/" + selectedsong)
        msg = "song: " + selectedsong
        pygame.mixer.music.play()
    if flag1 == "+":
        volume = volume + 0.2
        pygame.mixer.music.set_volume(volume)
    if flag1 == "-":
        volume = volume - 0.2
        pygame.mixer.music.set_volume(volume)
    if flag1 == "quit":
        exit(0)

pyglet.app.run()
