# action.py
import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My Name is Virtual Assistance")
        return "My name is virtual assistance"

    elif "hello" in user_data or "hye" in user_data :
        text_to_speech.text_to_speech("Hey, Sir How i can help you")
        return "hey, sir  how can i help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning Sir, How can i help you today")
        return "good morning sir, how can i help you today"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif"shutdown" in user_data:
        text_to_speech.text_to_speech("Ok sir")
        return "ok sir"

    elif"play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you")
        return "gaana.com is now ready for you"

    elif"Youtube" in user_data:
        webbrowser.open("https://Youtube.com/")
        text_to_speech.text_to_speech("Youtube.com is now ready for you")
        return "https://Youtube.com/ is now ready for you"


    elif"Open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"

    elif"weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    elif "show me" in user_data:
        capabilities = [
            "Tell you my name.",
            "Say hello or good morning.",
            "Tell you the current time.",
            "Shutdown the system.",
            "Play music on gaana.com.",
            "Open YouTube.",
            "Open Google.",
            "Tell you the weather for Koramangala."
        ]
        response = "Here are some things I can do:\n" + "\n".join(capabilities)
        text_to_speech.text_to_speech("Here are some things I can do.")
        return response


    else:
        text_to_speech.text_to_speech("Sorry Sir, I did not understand what you said")
        return "sorry sir, i did not understand what you said"
