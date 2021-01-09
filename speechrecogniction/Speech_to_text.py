import speech_recognition as sr
import pyaudio as pa
#import os
#print(os.getcwd())
filename = "male.wav"


recognizion = sr.Recognizer()
with sr.AudioFile(filename) as source:
    #reading audio
    print("in process of conversion")
    audio_data = recognizion.record(source)
    #converting to text
    print("recognizing...")
    try:
        text = recognizion.recognize_google(audio_data,language="es=US")

        print(text)
    except:
        print("No internet connection ! ")