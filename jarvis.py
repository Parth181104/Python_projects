import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding!!!")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

# speechtx("Hello , I love Python")

if __name__ == '__main__':
   

#    if sptext() == "hey Sam" :
       while True:
        data1=sptext()

        if "your name" in data1:
            name="My name is Sam"
            speechtx(name)
        elif "old are you" in data1:
            age = "I am two years old"
            speechtx(age)

        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'YouTube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke("en","neutral")
            speechtx(joke_1)
            
        elif 'play song' in data1:
            add = "D:\songs"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[0]))

        elif "exit" in data1:
            speechtx("Thank You")
            break
        time.sleep(5)
#    else:
#        print("thanks")
       



