import pyttsx3
engine=pyttsx3.init()
text=input("enter the text you want to convert to speech:")
engine.say(text)
engine.runaAndWait( )