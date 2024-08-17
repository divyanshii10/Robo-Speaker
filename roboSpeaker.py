
import pyttsx3 
  

command = pyttsx3.init() 
voices = command.getProperty('voices')
command.setProperty('rate', 120)
command.setProperty('volume', 2) 
command.setProperty('voice', voices[1].id)  
command.say("Welcome to roboSpeaker!") 
command.say("Created by Divyanshi kulshrestha") 
command.runAndWait() 
while True:
   x = input('Enter what would you like me to speak?')
   command.say(x)
   command.runAndWait()
   if x == 'q':
      command.say("Bye Bye dear!") 
      command.runAndWait()
      break
