# text_to_speech.py
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-70')
    engine.say(text)
    engine.runAndWait()


# Example usage (you can comment this out in your main project)
# text_to_speech("hello world")
