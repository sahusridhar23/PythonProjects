from mimetypes import init

import pyttsx3 as tts
#
# tts.init()
# tts.speak()

obj = init()
obj.say('Hello')
obj.setProperty(rate=150)