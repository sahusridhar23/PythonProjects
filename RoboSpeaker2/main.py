import pyttsx3

print("WELCOME TO ROBOSPEAKER 1.1, cerated by sridhar sahu")

while True:
    text = input('Enter what you want me to speak:')
    if text.lower() == 'q':
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say('bye bye friend')
        engine.runAndWait()
        engine.stop()
        del engine
        break
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine
