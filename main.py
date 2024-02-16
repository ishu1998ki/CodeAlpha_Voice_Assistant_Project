# In this project we need to install 3 libraries
# 1. SpeechRecognition
# 2. pyttsx3 (python text to speech library)
# 3. pywhatkit (to send the message by the Python script)

import speech_recognition as sr
import datetime
import subprocess
import pyttsx3
import pywhatkit
import wikipedia

# initiate engine for text-to-speech process
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# set voice for female
engine.setProperty('voice', voices[1].id)

# initiate speech recognition library
recognizer = sr.Recognizer()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def initiate_command():
    global command
    command = ""
    with sr.Microphone() as source:
        print(" Clearing background noises. I am listening..")
        # clearing background noises
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        # listen for the user's input
        recordedAudio = recognizer.listen(source)
        # using google to recognize audio
        try:
            command = recognizer.recognize_google(recordedAudio)
            command = command.lower()

            if 'alex' in command:
                command = command.replace('alex', "")
                print(command)
                return command
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return None


def play_command():
    command = initiate_command()
    print(command)

    if command is not None:
        if 'chrome' in command:
            a = 'Opening chrome...'
            talk(a)
            program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([program])

        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('The current time is ' + time)

        elif "play" in command:
            song = command.replace('play', "")
            talk("playing" + song)
            pywhatkit.playonyt(song)

        elif " who is" in command:
            name = command.replace('who is',"")
            information = wikipedia.summary(name,1)
            print(information)
            talk(information)

play_command()
