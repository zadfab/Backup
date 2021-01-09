import  gtts
from playsound import playsound

print("enter the text to convert in speech :")
text = input()
print("slow method try pyttsx module")
tts = gtts.gTTS(text)
tts.save("hello.mp3")
print("\n")
print("Playing...")
playsound("hello.mp3")