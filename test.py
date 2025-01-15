import struct
import time
import pvporcupine
import pyaudio
import pyautogui as autogui

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Initialize Porcupine with keywords
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"], sensitivities=[1, 0.7])
        
        # Initialize PyAudio
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
        )
        
        print("Listening for hotwords...")

        # Infinite loop to process audio
        while True:
            # Capture the start time
            start_time = time.time()

            # Read audio data from the stream
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # Process the audio and check for hotwords
            keyword_index = porcupine.process(keyword)

            # Capture the end time
            end_time = time.time()

            # Calculate the time it took to process the audio
            processing_time = end_time - start_time
            print(f"Processing Time: {processing_time:.3f} seconds")

            # If a keyword was detected, trigger the action
            if keyword_index >= 0:
                detected_word = ["jarvis", "alexa"][keyword_index]
                print(f"Hotword detected: {detected_word}")
                
                # Perform action: Press shortcut key (Win + J)
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except Exception as e:
        print(f"An error occurred: {e}")
    

# Run the hotword detection function
hotword()
