import os

def speak(text):
    os.system(
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
    )

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.0. Created by Harry")


while True:
    x = input("Enter what you want me to speak: ")

    if x.lower() == "q":
        speak("bye bye friend")
        break

    speak(x)
