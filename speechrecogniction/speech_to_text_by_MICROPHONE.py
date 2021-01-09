import speech_recognition as sr

recognizer = sr.Recognizer()
print("say...")
with sr.Microphone() as source:
    audio_data = recognizer.record(source, duration=5)
    print("Recognizing...", end="\n\n")
    try:
        text = recognizer.recognize_google(audio_data, language="en-US")
        print("Did you said  " + "'" + text + "'")
    except:
        print("No internet connection !")
