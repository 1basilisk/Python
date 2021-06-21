import pyttsx3

pyttsx3.engine = pyttsx3.init("espeak")
name = input("What's your name? ")
pyttsx3.engine.say(f"hello, {name}")
pyttsx3.engine.runAndWait()
