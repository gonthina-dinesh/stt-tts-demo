import whisper

def transcribe_with_whisper(file_path):
    print("Transcribing strated...")
    model = whisper.load_model("base")  # or "small", "medium", "large"
    result = model.transcribe(file_path)
    print("📝 Transcription:")
    print(result['text'])

if __name__ == "__main__":
    transcribe_with_whisper('audio.wav')
