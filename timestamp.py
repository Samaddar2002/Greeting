import time
import pyttsx3

def speak(s):
    e=pyttsx3.init()
    e.say(s)
    e.runAndWait()

def greeting():
  timestamp=time.strftime('%H:%M:%S')
  hour=int(time.strftime('%H'))

  if (5 <= hour < 12 ):
    return "Good Morning Dear!"
  elif (12 <= hour < 16):
    return "Good Afternoon Dear!"
  elif (16 <= hour < 20):
    return "Good Evening Dear!"
  else:
    return "Good Night Dear!"
 
p=greeting()
print(p)
speak(p)