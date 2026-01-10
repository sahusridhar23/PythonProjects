import pyttsx3

print("WELCOME TO ROBOSPEAKER 1.1, cerated by sridhar sahu")
engine = pyttsx3.init()
engine.setProperty('rate',150)

while True:
    text = input('Enter what you want me to speak:')
    if text.lower() == 'q':
        engine.say('bye bye friend')
        engine.runAndWait()
        break
    engine.say(text)
    engine.runAndWait()
