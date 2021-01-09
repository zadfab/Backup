import  pyttsx3

engine = pyttsx3.init()

run = "this program is written by zad , enjoy"
engine.say(run)
engine.runAndWait()
text = input("enter text to convert in speech : ")

engine.say(text)
engine.runAndWait()