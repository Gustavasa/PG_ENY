import webbrowser
name = "Erik"
state="michigan"
city="quatemala"
tvshow="flash"
composer="hans zimmer"
book = "LOTR"
password= "erik"
url= "https://www.google.com/search?q=memes&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi_iaDwytfWAhUK2oMKHbq8BgUQ_AUICigB&biw=1034&bih=615"

print( name + " likes to visit " + state+ " and " + city)
print("He also likes to read " + book + " and always watches " + tvshow)
print("He loves listening to music by " + composer)

print("Whats your favorite subject")
subject = input()

if subject == "history" or subject == "math":
    print("wow you are Erik")
else:
    print("i hope you get the password right")

print("what is the pasword")

code= input ()
if code == password:
    print("you are in")
    webbrowser.open_new(url)
else:
    print("you die")
