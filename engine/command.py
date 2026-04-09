import pyttsx3
import speech_recognition as sr
import eel
import time
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 174)
def speak(text):
    text = str(text)

    eel.ShowSiriWave()   # 🔥 show speaking UI

    eel.DisplayMessage(text)
    eel.receiverText(text)

    engine.say(text)
    engine.runAndWait()

    eel.ShowHood()       # 🔥 go back after speaking

@eel.expose
def stopSpeaking():
    engine.stop()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.senderText(query)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        if query == "":
            return
        eel.senderText(query)
    else:
        query = message.lower()
        eel.senderText(query)

    try:
        # TIME
        if "time" in query:
            from datetime import datetime
            speak(datetime.now().strftime("%H:%M"))

        # DATE
        elif "date" in query:
            from datetime import datetime
            speak(datetime.now().strftime("%d %B %Y"))

        # OPEN
        elif "open" in query:
            from engine.features import openCommand
            openCommand(query)

        # YOUTUBE
        elif "youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "stop" in query or "stop speaking" in query:
            engine.stop()
            speak("Stopped")
            return

        # AI fallback
        else:
            from engine.features import geminai
            geminai(query)

    except Exception as e:
        print("error:", e)
        speak("Something went wrong")
    eel.ShowHood()