import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib  # built-in library
import webbrowser as wb  # built-in library
import os  # built-in library
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # to convert time into a string format
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)  # Initially it is a string hence typecasting it to int
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)


def WishMe():
    speak("Welcome back Ekveera")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour <= 17:
        speak("Good afternoon")
    elif hour > 17 and hour <= 24:
        speak("good evening")
    else:
        speak("Good night")
    speak("Ojus at your Service. Please tell me how can I help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Sorry, please say that again")
        return "none"

    return query


def search(query):
    query = query.split(' ')
    query = " ".join(query[0:])
    print(query)
    result = wikipedia.summary(SpeechHeard, sentences=2)
    print(result)
    speak(result)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # Lines 72 and 73 are used for checking up the connection with gmail
    server.starttls()
    server.login('eku2410@gmail.com',
                 '10088001')  # logins into our account, but enable 'less secure apps' in gmail account first.
    speak("Successful login")
    server.sendmail('eku2410@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()  # built in function in pyautogui library
    img.save('C:\\Users\\HP\\Pictures\\Screenshots\\ss.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()  # returns a list
    speak("battery percentage is")  # cannot concatenate
    speak(battery.percent)
    speak("percent")


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    WishMe()
while True:
    SpeechHeard = takeCommand()
    if 'time' in SpeechHeard:
        time()

    elif 'date' in SpeechHeard:
        date()

    elif 'search' in SpeechHeard:
        speak("Searching right away mam...")
        search(SpeechHeard)

    elif 'open a website' in SpeechHeard:
        speak("Which website should I open Mam?")
        chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # adding a path for chrome browser.
        website = takeCommand().lower()
        wb.get(chromepath).open_new_tab(
            website + '.com')  # opens up the browser and then makes a search for the website on a new tab.

    elif 'send email' in SpeechHeard:
        try:
            speak("What should I say mam?")
            content = takeCommand()
            print(content)
            speak("Whom should I send this to?")
            to = takeCommand().lower()
            to = to.replace(" ", "")
            print(to)
            speak("Okay, sending..")
            sendEmail(to, content)
            speak("Email has been successfully sent.")
        except Exception as e:
            print(e)
            speak("Unable to send.")

    elif 'logout' in SpeechHeard:
        speak("Mam are you sure?")
        permission = takeCommand()
        if permission == "no":
            speak("Alright.")
            continue
        else:
            speak("okay,logging out")
            os.system("shutdown -l")

    elif 'restart' in SpeechHeard:
        speak("Mam are you sure?")
        permission = takeCommand()
        if permission == "no":
            speak("Alright.")
            continue
        else:
            speak("okay,restarting the computer")
            os.system("shutdown /r /t 1")

    elif 'shutdown' in SpeechHeard:
        speak("Mam are you sure?")
        permission = takeCommand()
        if permission == "no":
            speak("Alright.")
            continue
        else:
            speak("okay,shutting down")
            os.system("shutdown /s /t 1")

    elif 'play a song' in SpeechHeard:
        songs_dir = 'E:\One Direction'
        songs = os.listdir(songs_dir)
        speak("Which song number would you like to hear?")
        song_no = int(takeCommand())
        print(song_no)
        os.startfile(os.path.join(songs_dir, songs[song_no]))
        quit()

    elif 'remind me' in SpeechHeard:
        speak("Remind you what mam?")
        data = takeCommand()
        remember = open('data.txt', 'w')  # 'w' is for write format
        remember.write(data)
        remember.close()
        speak("okay sure")

    elif 'to remember' in SpeechHeard:  # what did I ask you to remember
        remember = open('data.txt', 'r')
        filesize = os.stat('data.txt').st_size
        if filesize == 0:
            speak("There is nothing you asked me to remember, I am afraid.")
        else:
            speak("You asked me to remember that" + remember.read())
            thankYou = takeCommand()
            speak("You are welcome")

    elif 'screenshot' in SpeechHeard:
        screenshot()
        speak("Done")

    elif 'battery status' in SpeechHeard:
        cpu()

    elif 'joke' in SpeechHeard:
        jokes()

    elif 'go offline' in SpeechHeard:
        speak("Signing off")
        quit()
