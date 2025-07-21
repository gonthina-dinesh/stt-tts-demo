# STT-TTS Demo (Speech-to-Text & Text-to-Speech)

This project demonstrates:
- **TTS (Text-to-Speech)** using `pyttsx3`
- **STT (Speech-to-Text)** using `whisper`

##  How to Run with Docker Compose

### 1. Clone the Repository
```bash
git clone https://github.com/gonthina-dinesh/stt-tts-demo.git
cd stt-tts-demo
```

### 2. Run the Containers

#### For Text-to-Speech (TTS)
```bash
docker compose run --rm tts
```

#### For Speech-to-Text (STT)
```bash
docker compose run --rm stt
```

---

##  Files

- `tts.py`: Converts text input to `output.wav`
- `stt.py`: Converts `input.wav` to text using Whisper

##  Notes

- Input/output `.wav` files are stored inside the container (`/app`).
- You can mount volumes if needed to access them locally.
