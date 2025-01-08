import os
import re
import playsound as playsound
import eel
import pywhatkit as kit
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.db import cursor
#playing assistant  sound function
"""@eel.expose
def playAssistantsound():
    music_dir="www\\assets\\audio\\start_sound.mp3"
     playsound(music_dir) """
def openCommand(query):
    query=query.replace(ASSISTANT_NAME, "")
    query=query.replace("open","")
    query.lower()
    

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+"on Youtube")
    kit.playonyt(search_term)
def extract_yt_term(command):
    # define a regular expression pattern to extract song name
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    #use re.search to find a match in the command
    match=re.search(pattern,command,re.IGNORECASE)
    #if a match is found return the extracted song name ;otherwise none
    return match.group(1) if match else None
