import pyttsx3
import os

def speak_to_file(text, filename="output.wav"):
    full_path = os.path.join(os.getcwd(), filename)  # Ensures it saves inside /app
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1.0)

    # Set voice (optional – you can skip this)
    voices = engine.getProperty('voices')
    try:
        engine.setProperty('voice', voices[28].id)
    except Exception as e:
        print(f"⚠️ Failed to set voice: {e}")

    # 🔈 Save to file instead of speaking
    print(f"\n💾 Saving speech to: {filename}")
    engine.save_to_file(text, full_path)
    engine.runAndWait()

if __name__ == "__main__":
    input_text = input("Enter text to speak: ")
    speak_to_file(input_text, "output.wav")
