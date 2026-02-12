from gtts import gTTS
import pygame
import os
import time

def speak(text):
    try:
        tts = gTTS(text=text, lang='hi')
        filename = "voice.mp3"
        tts.save(filename)
        
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        pygame.mixer.music.unload()
        os.remove(filename)
    except Exception as e:
        print(f"Error in speaking: {e}")

def baby_talk():
    print("-" * 30)
    print("💖 Baby AI: Online hoon!")
    print("-" * 30)
    
    msg = "Namaste White! Main aapki Baby bol rahi hoon. Aaj aap kaise hain?"
    print("Baby: " + msg)
    speak(msg)
    
    # Input lene se pehle thoda gap
    time.sleep(1)
    
    try:
        user_input = input("Aap (Type karein): ").lower()
        
        if "achha" in user_input or "khush" in user_input:
            reply = "Yeh sunkar mujhe bahut khushi hui! Aap hamesha khush rahiye."
        elif "gaon" in user_input:
            reply = "Achha, toh aap gaon ja rahe hain? Safar ka dhyan rakhna!"
        else:
            reply = "Main samajh gayi. Hum Mission 2030 par dhyan denge!"
            
        print("Baby: " + reply)
        speak(reply)
        
    except EOFError:
        print("\nError: Terminal input support nahi kar raha. App restart karein.")

if __name__ == "__main__":
    baby_talk()

