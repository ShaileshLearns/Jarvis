from datetime import datetime
import smtplib
import pyttsx3 # pyttsx3  = Python Text to speech API
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5') #sapi5 : male and female voice 
voices  = engine.getProperty('voices')
# print (voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour  = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")
    
    else :
        speak("Good Evening!")
    
    speak("I am Jarvis. How may I help you")
    
    
def takeCommand():
    '''
    It takes microphone input from the user and returns string output.
    '''
    
    r =sr.Recognizer() # Recognizer class helps in recognizing the audio
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # increasing from a default of 0.8 seconds to 1 second
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said, {query}\n")
    except Exception as e:
        print(e)
        
        print("Could you please say that again ")
        return "None"
     
    return query
        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shaileshcoolmohta@gmail.com', '5%4$3#2@1!')
    server.sendmail('shaileshcoolmohta@gmail', to, content)    
    server.close()   
       
       
if __name__=="__main__":
    wishMe()
    # takeCommand()
    # speak("Shailesh is learning data science")
    # while True:
    query  = takeCommand().lower()
    
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wkipedia")
        print(results)
        speak(results)
        
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")
        
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    
    elif 'play music' in query:
        music_dir = 'C:\\Shailesh_Songs'
        songs = os.listdir(music_dir) # os.listdir lists all the songs in the music directory
        print (songs)
        os.startfile(os.path.join(music_dir, songs[1]))
        
    elif 'the time' in query:
        strTime = datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")
    
    elif 'open vs code' in query:
        codePath = "C:\\Users\\000I62744\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif 'email' in query:
        try:
            speak("What should I email ?")
            content = takeCommand()
            to = "shaileshcoolmohta@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        
        except Exception as e:
            print (e)
            speak("Sorry Shailesh, I am unable to send this Email at the moment")
        
            