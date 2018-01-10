import time
# Reverse Cipher

 # https://www.nostarch.com/crackingcodes/ (BSD Licensed)

print(" give me a message")


message = input()
translated = ''

i = len(message) - 1


while i >= 0:
    translated = translated + message[i]
    print('i is', i, ', message[i] is', message[i], ', translated is',
        translated)
    i = i - 1
    time.sleep(.1)
print(translated)

