from easygui import *
from playsound import *
from pydub import AudioSegment
import pyglet

msg = "song:"

btns = ["paus", "play", "quit"]

music = pyglet.resource.media('1.mp3')



while True:
    flag1 = buttonbox(msg,choices = btns)
    if flag1 == "play":
        music.play()
    if flag1 == "paus":
        print("music is now paused")
    if flag1 == "quit":
        exit(0)

pyglet.app.run()
