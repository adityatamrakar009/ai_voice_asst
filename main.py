import os
import openai
from openaiapi import get_chatgpt_response
from elevenlabsapi import apikey
import io
import requests
from pydub import AudioSegment
from pydub.playback import play

# Custom directory for saving text files
output_text_directory = "C:/Users/dom/outputs2"  # Text directory

# Eleven Labs API and Voice ID - "TmQmj1rrc2pDH2JOOfTi"
ELEVEN_LABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech/TmQmj1rrc2pDH2JOOfTi"
ELEVEN_LABS_API_KEY = apikey

def text_to_speech(text):
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_LABS_API_KEY,
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
    }

    response = requests.post(ELEVEN_LABS_API_URL, json=data, headers=headers)
    
    audio = AudioSegment.from_mp3(io.BytesIO(response.content))
    play(audio)  # Play the audio
    
def save_response_to_file(prompt, response):
    with open(
        os.path.join(output_text_directory, "output.txt"),
        "a",
        encoding="utf-8",
    ) as text_file:
        text_file.write(f"Prompt - {prompt}\nResponse - {response}\n\n")

print("Alfred: Fuck You Master Wayne")
text_to_speech("Fuck You Master Wayne")
user_input = input("Master Wayne: ")
response = get_chatgpt_response(user_input)

text_to_speech(response) # ChatGPT Response as audio
save_response_to_file(user_input, response) # Saving ChatGPT response and the prompt in a single text file
print("Alfred:", response)
