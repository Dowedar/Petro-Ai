import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import pyjokes
import matlab.engine



engine = pyttsx3.init()
eng = matlab.engine.start_matlab()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
    if voice == 2:
        engine.setProperty('voice',voices[1].id)


def time():  
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # hours , Minutes , Seconds
    speak("The current time is")
    speak(Time)


def date(): 
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('the current date is ')
    speak(month)
    speak(day)
    speak(year)


def greeting():   
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak('good morning sir!')
    elif 12 <= hour < 18:
        speak('good afternoon sir!')
    elif 18 <= hour < 24:
        speak('good evening sir!')
    else:
        speak('good night sir!')


def wishme():     
    greeting()
    speak('PETRO AI at your service , please tell me how can i help you?')




def takecomandmic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listing...')
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="en-GB")
    except Exception as e:
        print(e)
        speak('Say that again please...')
        return 'None'
    return query

def search_one_petro():
    speak('what should I search for?')
    search = takecomandmic()
    wb.open('https://onepetro.org/search-results?page=1&q='+search)


def prid():
    speak('please enter the required inputs in the terminal')
    x1 = float(input('Enter The Depth\n'))
    x2 = float(input('Enter The Gama_Ray\n'))
    x3 = float(input('Enter The Neutron_Porosity\n'))
    x4 = float(input('Enter The Resistivity\n'))
    x5 = float(input('Enter The Bulk_denisty\n'))
    x=round(eng.prediction(x1,x2,x3,x4,x5))
    speak(f'the pore pressure is {x} PSI')
    print(x)






if __name__ == "__main__":
    getvoices(1)
    wishme()
    while True:
        query = takecomandmic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        elif 'search' in query:
            search_one_petro()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'predict' in query:
            prid()
        elif 'off' in query:
            speak('procees the shut down')
            quit()
