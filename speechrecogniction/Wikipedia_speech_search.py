import  wikipedia
import speech_recognition as sr
import pyttsx3


def search(query):
    print("in search ...")


        # If the query cannot be searched using
    # WolframAlpha then it is searched in
    # wikipedia

    print("searching in wikipedia")
    query = query.split(' ')
    query = " ".join(query[0:])

    SpeakText("I am searching for " + query)
    print(wikipedia.summary(query, sentences = 3))
    SpeakText(wikipedia.summary(query,sentences = 3))


    # Function to convert text to
# speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

query = ""
# Driver's code
# input query from the user by
# typing or by voice


# if query is blank then user
# is prompted to speak something.
if query == '':
    r = sr.Recognizer()

    # uses the default microphone
    # as the source to record voice
    with sr.Microphone() as source:
        print("Say Something ")

        # reduces the background disturbances
        # and noise for 2 seconds

        r.adjust_for_ambient_noise(source, 1)
        print("Removing noises")
        # listening to source
        audio = r.listen(source)
    try:
        print("recognizing")
        speech = r.recognize_google(audio)
        search(speech)

        # Handling Exceptions if speech
    # is not understood.
    except sr.UnknownValueError:
        print("Google Speech Recognition could not \
        understand audio")

        # Couldn't handle requests, occurs
        # mainly because of network errors
    except sr.RequestError as e:
        print("Could not request results from Google \
        Speech Recognition service;{0}".format(e))
else:
    search(query)