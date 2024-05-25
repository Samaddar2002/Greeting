import datetime
import pyttsx3

t=datetime.datetime.now()
timestamp=t.hour
e=pyttsx3.init()

if (5 <= timestamp < 12 ):
    print("Good Morning")
    speak="Good Morning"
elif (12 <= timestamp < 16):
    print("Good Afternoon")
    speak="Good Afternoon"
elif (16 <= timestamp < 20):
    print("Good Evening")
    speak="Good Evening"
else:
    print("Good Night")
    speak="Good Night"

e.say(speak)
e.runAndWait()