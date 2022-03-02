from copy import copy
from email.mime import audio
from turtle import left, position
import pyautogui as pt
import pyperclip as pc
import pyaudio 
from pynput.mouse import Button, Controller
from time import sleep
import pyttsx3
import requests
import jokes
from requests import get
from json import loads



import speech_recognition as sr

r=sr.Recognizer()
pt.FAILSAFE=True
mouse=Controller()

#nav
def nav_to_image(image, clicks, off_x=0,off_y=0):
    position = pt.locateCenterOnScreen(image,confidence=0.7)

    if position is None:
        print(f'{image} not found')
    else:
        pt.moveTo(position,duration=0.5)
        pt.moveRel(off_x,off_y,duration=0.2)
        pt.click(clicks=clicks,interval=0.1)



def get_msg():
    nav_to_image(r'images/clip.png',0, off_y=-80,off_x=50)
    mouse.click(Button.left,3)
    pt.rightClick()
    copy=nav_to_image(r'images/copy.png',1)
    sleep(0.5)
    return pc.paste() if copy !=0 else 0
def send_msg(msg):
    nav_to_image(r'images/clip.png',0, off_y=0,off_x=80) 
    pt.typewrite(msg,interval=0.01)
    pt.typewrite("\n",interval=0.01)
    print(msg)
    
def process(msg):
    raw_msg=msg.lower()
    if raw_msg == 'quote':
        qt=get_random_quote()
        return qt
    elif raw_msg == "yes":
        return 'bot says u said yes'
    elif 'quote' in raw_msg:
        qt=get_random_quote()
        return qt
    elif 'joke' in raw_msg:
        qt=jokes.random()
        print(qt)
        pt.typewrite(qt["category"],interval=0.01)
        pt.typewrite("\n")
        if(qt["type"]=='twopart'):
            pt.typewrite(qt["setup"],interval=0.01)
            pt.typewrite("\n")
            pt.typewrite(qt["delivery"],interval=0.01)
            pt.typewrite("\n")
        else:
            pt.typewrite(qt["joke"],interval=0.01)
            pt.typewrite("\n")
        return "LOL"
    


def open_read():
    x=True
    while x==True:
        nav_to_image(r'images/unrd.png',0, off_y=0,off_x=-80)
        mouse.click(Button.left,1)
        x=False




def get_random_quote():
    response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    return ('{quoteText} - {quoteAuthor}'.format(**loads(response.text)))
msg=""
open_read()
send_msg(process(get_msg()))
