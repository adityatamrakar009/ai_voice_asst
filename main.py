import os
import openai
from openaiapi import get_chatgpt_response
import requests
from elevenlabsapi import apikey
from pydub import AudioSegment
from pydub.playback import play
import io

# Custom directory for saving audio and text file
output_directory = "C:/Users/dom/outputs"  # Audio directory
output_text_directory = "C:/Users/dom/outputs2"  # Text directory

# Eleven Labs API and Voice ID - "TmQmj1rrc2pDH2JOOfTi"
ELEVEN_LABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech/TmQmj1rrc2pDH2JOOfTi"
ELEVEN_LABS_API_KEY = apikey


def text_to_speech(text, save=True):
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

    # Extract the first five words to create a unique identifier
    words = text.split()
    response_identifier = "_".join(words[:5])

    if save:
        output_audio_path = os.path.join(
            output_directory, f"{response_identifier}_output.mp3"
        )

        # Save the generated audio with the unique identifier
        audio = AudioSegment.from_mp3(io.BytesIO(response.content))
        audio.export(output_audio_path, format="mp3")

    # Play the generated audio unless save is False
    if save:
        play(audio)

    return response_identifier


def save_response_to_file(response_text, response_identifier):
    with open(
        os.path.join(output_text_directory, f"{response_identifier}_output.txt"),
        "w",
        encoding="utf-8",
    ) as text_file:
        text_file.write(response_text)


print("Alfred: Welcome back, Master Wayne")
text_to_speech("Welcome back, Master Wayne", save=False)

user_input = input("Master Wayne: ")
response = get_chatgpt_response(user_input)

# Save the ChatGPT response to a text file with the unique identifier
response_identifier = text_to_speech(response)
print("Alfred:", response)

# Check if the response_identifier is None (indicating it's the welcome message)
if response_identifier is not None:
    save_response_to_file(response, response_identifier)
