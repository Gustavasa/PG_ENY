name="kire"

subject= ["Viper", "Python", "Anaconda", "Sidewinder"]

print("Hello " + name)

for i in subject:
    if i == "Python":
        print("The " + i + " is the best ship in the game.")
    elif i == "Sidewinder":
        print("The " + i + " is the worst ship in the game")
    else:
        print("The " + i + " is a good ship")
    
movies = []

while True:
    print("What's a movie you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)
for i in movies:
    print("one of you favorite movies is " + i)
