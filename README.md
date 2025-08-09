AI Assistant
This project is a desktop AI assistant built with Python and the tkinter library, providing a graphical user interface (GUI) for interaction. The assistant can respond to both voice and text commands, performing various tasks such as telling the time, opening websites, and retrieving weather information. It serves as an excellent demonstration of integrating different Python libraries to create a functional and interactive application.

Key Features
GUI Interface: A clean and simple graphical user interface built with tkinter.

Voice & Text Input: Interact with the assistant using either your voice (via the "ASK" button) or a text box (via the "Send" button).

Predefined Commands: The assistant can respond to a variety of commands, including:

Telling the current time.

Opening websites like Google, YouTube, and Gaana.com.

Providing a list of its capabilities.

Retrieving and speaking the current weather for a specific location.

Text-to-Speech Output: All responses from the assistant are read aloud using a text-to-speech engine.

Conversation Log: The assistant's and user's messages are displayed in a scrollable text area.

Skills Demonstrated
Python Programming

GUI Development (tkinter)

Speech Recognition (speech_recognition library)

Text-to-Speech (pyttsx3 library)

Web Scraping (requests-html library for weather data)

System Automation (webbrowser module)

Modular Code Design (separation of logic into different files)

Image Handling (PIL - Pillow library)

Prerequisites
To run this project, you will need Python 3.x installed on your system.

Python Libraries
You can install all the required Python packages using pip:

pip install speechrecognition pyttsx3 requests-html Pillow

Note on Microphone
This project requires a working microphone to use the voice command feature. You may also need to install pyaudio for speech_recognition to work correctly.

File Structure
This project is organized into several modules, each responsible for a specific function:

GUI.py: The main script that creates the user interface and handles button clicks.

action.py: Contains the core logic for processing user commands and deciding on a response.

speech_to_text.py: A helper module for converting spoken language into text.

text_to_speech.py: A helper module for converting text responses into speech.

weather.py: A helper module that scrapes Google for weather information.

Installation and Usage
Clone the Repository:
First, clone this repository to your local machine using git.

git clone https://github.com/Sagarrajjj/Desktop_Assistant.git

Install Dependencies:
Make sure you have all the required libraries installed.

Place Image:
The GUI requires an image file named assitant.png in a subdirectory called image. Create this directory and place your image there, or update the path in GUI.py.

Run the Script:
Execute the main Python script from your terminal:

python GUI.py

The GUI window will appear, and you can begin interacting with the assistant.

Troubleshooting
FileNotFoundError for assitant.png: Ensure you have created the image directory and placed your assitant.png file inside it.

ModuleNotFoundError: Double-check that all required libraries are installed. The command pip install speechrecognition pyttsx3 requests-html Pillow should resolve most issues.

Voice commands not working: Make sure your microphone is properly configured and that you have installed pyaudio if needed.

Weather data retrieval fails: Google's HTML structure can change, which may break the web scraping logic in weather.py. If this happens, the script will return a friendly error message.

License
This project is licensed under the MIT License.
