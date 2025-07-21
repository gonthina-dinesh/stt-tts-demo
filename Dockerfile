# Use base image with Python
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    espeak \
    espeak-ng \
    ffmpeg \
    libespeak1 \
    libportaudio2 \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all local files into container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install torch scipy sounddevice pyttsx3
RUN pip uninstall -y whisper && pip install git+https://github.com/openai/whisper.git

# Set default command (you can change this to tts.py if needed)
CMD ["python", "stt.py"]
