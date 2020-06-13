import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pyttsx3
import time
import os
import Extracting_Google_Sheets


r = sr.Recognizer()

#Defining text-to-speech
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   #Change voices, 0 for Male and 1 for Female voice
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Listening to voice input and providing responses if error
def Speech_Read(ask = False):
    with sr.Microphone() as source:
        print('listening...')
        if ask:
            print(ask)
        r.adjust_for_ambient_noise(source, 1)       #You can always remove noise cancellation feature and pause
        audio = r.listen(source)
        voice_data = ""
    try:
        voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("I am sorry, I didn't get that")
        """speak("I am sorry, I didn't get that")"""
    except sr.RequestError:
        print("My server is down, Try again later!")
        speak("My server is down, Try again later!")
    return voice_data

#Defining specific Commands/tasks
def respond(voice_data):
    query = Speech_Read()
    if "what is your name" in voice_data:
        print("My name is Junior") 
        speak("My name is Junior")
    if "time" in voice_data:
        print(str(datetime.datetime.now()) + " hours!") 
        speak(str(datetime.datetime.now()) + " hours!")
    if "search" in voice_data:
        speak('what do you want to search?')
        search = Speech_Read("what do you want to search?")
        url = ('https://google.com/search?q=' + search)
        webbrowser.get().open(url)
        print('Here is what I found for ' + search) and speak('Here is what I found for ' + search)
    
    if "history" in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        print(results) 
        speak(results)

    if 'find location' in voice_data:
        output = Speech_Read('which place do you want to find?')
        webbrowser.get().open(speak('https://www.google.com/maps/place/' + output))
        print('Here is what I found for ' + output) 
        speak('Here is what I found for ' + output)
    if 'open video' in voice_data:
        webbrowser.open("https://youtube.com")
        print('opening YouTube...') 
        speak('opening YouTube...')
    if 'play me a song' in voice_data:
        songs = os.listdir('C:\\Users\\USER\\Music')
        os.startfile(os.path.join('C:\\Users\\USER\\Music', songs[0]))
        speak('playing...')
    if 'open design' in voice_data:
        os.startfile('C:\\Program Files\\Autodesk\\Revit 2020\\Revit.EXE')
        print('opening Autodesk Revit...') and speak('opening Autodesk Revit...')

        #Here I extracted data from a Google sheet which can only be accesesed by Me, You can make edits to suite your purpose
    if 'check temperature' in voice_data:
        print('temperature is ' + str(Extracting_Google_Sheets.cell) + ' degree celcius')
        speak('temperature is ' + str(Extracting_Google_Sheets.cell) + ' degree celcius')

    if 'stop program' in voice_data:
        print('Goodbye!...')
        speak('Goodbye!')
        exit()
   #Please, feel free to add more commands 
    
#Greets you with     
def GreetMe():
    hours = datetime.datetime.now().hour
    if hours >= 0 and hours < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hours >= 12 and hours < 16: 
        print("Good Afternoon!")
        speak("Good Afternoon!")
    elif hours > 16 and hours < 20: 
        print("Good Evening!")
        speak("Good Evening!")
    elif hours > 20 : 
        print("Good Night!")
        speak("Good Night!")
GreetMe()



time.sleep(1)
#speak('initializing...')   #You can make it say initializing at every start by uncommenting
print('I am your Assistant, How can I help you?!') 
speak('I am your Assistant, How can I help you?!')   
while 1:
    voice_data = Speech_Read()
    respond(voice_data)



#Please feel free to improve, add more features and modify to suite your purpose. Ibrahim Shittu
 