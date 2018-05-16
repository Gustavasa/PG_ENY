password="j"

import webbrowser

url="https://www.youtube.com/watch?v=PfYnvDL0Qcw"

lulu="https://www.youtube.com/watch?v=fVtkAGJvNu8"

print("what is your name?")
name = input()

if name == "Erik":
    print("Hello, Erik what is the password?")
    answer=input()
    if answer==password:
        print("You are in enabling site")
        webbrowser.open_new(url)
    else:
        print("Not correct, access denied")
        webbrowser.open_new(lulu)
        
    
    
    
else:
    
    print("Hello," + name + " what is the password?")
    answer=input()
    if answer==password:
        print("You are in enabling site")
        webbrowser.open_new(url)
    else:
        print("Not correct, access denied")
        webbrowser.open_new(lulu)
    

