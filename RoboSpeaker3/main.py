import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

print("WELCOME TO ROBOSPEAKER 1.3 ,created by sridhar sahu.")

while True:
    text = input("Enter the text you want to speak: ")
    if text.lower() == 'q':
        speak.Speak("bye bye friend")
        break
    speak.Speak(text)

