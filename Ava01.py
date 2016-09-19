import talkey
import os
import chatterbot
from chatterbot import ChatBot
import nltk

def speak(text):
    voice = talkey.Talkey(engine_preference=['pico'])
    voice.say(text+'........')


