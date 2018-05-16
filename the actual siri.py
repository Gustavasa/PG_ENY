import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hello Erik how can I help you")
    print("listening...")
    audio = r.listen(source)
    print("thinking...")



try:
    words = r.recognize_google(audio)
    speak.Speak("Lets go and look for" + r.recognize_google(audio))
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    speak.Speak("what are you saying")

except sr.RequestError as e:
    speak.Speak("nope")
