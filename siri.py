import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What video do you want to watch")



answer = pg.prompt("Enter video name")

speak.Speak("Ok lets look for" + answer)

wb.open("https://www.youtube.com/results?search_query=" + answer)
