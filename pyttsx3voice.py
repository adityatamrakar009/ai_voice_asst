import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
for voice in voices:
    print("Voice:", voice.name)

# Set the desired voice
selected_voice = "Microsoft David Desktop - English (United States)"
engine.setProperty("voice", selected_voice)

engine.say("This is a fucking test you bastard.")
engine.runAndWait()
