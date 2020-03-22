import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
 
from playsound import playsound

import sys,time,random



print("Initializing Assisstant...")

MASTER = "sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
rate = engine.setProperty("rate",192)
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12 :
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18 :
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)


def slow_type(t):
    typing_speed = 70 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

def takeCommand():
    playsound("F://Jarvis//sound//open_talk.mp3")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        playsound("F://Jarvis//sound//close_talk.mp3")
        
    try :
        print("Recognition....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Please Say that again" + MASTER)
        query= None

    return None

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('address@gmail.com','password')
    server.sendmail("recipeanMail",to , content)

def my_function():
    with open("123.txt",'r') as f, open('output.txt','w') as fw:
        text = f.read()
        result_string = ''
        
        words =['what is AI']
        text2 = text.split('.')
        for itemIndex in range(len(text2)):            
            for word in words:
                if word in text2[itemIndex]:
                    if text2[itemIndex][0] == ' ':
                        print(text2[itemIndex][1:])
                        result_string += text2[itemIndex][1:]+'.'
                        break
                    else:
                        print(text2[itemIndex])
                        result_string += text2[itemIndex]
                        break
        #print(result_string)
        fw.write(result_string)
                        
                
        


def main():

    speak("Initializing Assisstant...")
    speak('importing perferences and calibrating virtual environment')
    speak('all..done')
    wishMe()    
    playsound("F://Jarvis//sound//open_talk.mp3")
    query = input("What's on your mind?: ")
    playsound("F://Jarvis//sound//close_talk.mp3")
    
    
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia....')
        print('Searching wikipedia....')
        query = query.replace("wikipedia","")
        results =wikipedia.summary(query, sentences=3)                 
        speak(results)
        slow_type(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open("youtube.com")
        url = "youtube.com"
        youtube_path = 'c:/Program File (x86)/Google/Chrome/Application/Chrome.exe %s'
        webbrowser.get(youtube_path).open(url)

    elif 'open chrome' in query.lower():
        #webbrowser.open("youtube.com")
        url = "google.com"
        chrome_path = 'c:/Program File (x86)/Google/Chrome/Application/Chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "E:\\songs\\2.0"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'time now' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")        
        speak(f"the time is {strTime}")
        
    elif 'are you there' in query.lower():
        speak("At you service.."+ MASTER)
        
    elif 'bye' or 'shutdown yourself' in query.lower():
        speak('bye..bye..and have a good day..'+ MASTER)
        
    elif 'check on control surface' in query.lower():
        speak("will do.."+ MASTER)
        speak('...i have indeed been uploaded,...'+ MASTER +'...we are online and  ready..')
        
    elif 'send email' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            speak("to whom i need to send")
            to = takeCommand()
            sendEmail(to, content)
            speak("Email has been sent successfully" + MASTER)
        except Exception as e:
            speak(e)
            
    elif 'volume' in query.lower():
        if 'low volume' in query.lower:
            n=1.0
            n =n-1
            engine.setProperty('volume',n)
            speak("is it ok"+ MASTER)
            a = takeCommand()
            if a=="ok" or "yes" or "perfect":
                speak('on set'+ MASTER)
            else:
                speak('decresing')
        elif 'rise volume' in query.lower:
            n=1.0
            n =n+1
            engine.setProperty('volume',n)
            speak("is it ok"+ MASTER)
            a = takeCommand()
            if a=="ok" or "yes" or "perfect":
                speak('on set'+ MASTER)
            else:
                speak('increasing')

main()



   
    
    
