📽️ Auto-Subtitle-Generator

Simple Python tool to automatically generate subtitle (.srt) files from video files using OpenAI Whisper.

This script loads a Whisper model, transcribes the audio of a video, and produces a standard .srt subtitle file with timestamps.

🚀 Features

🗣️ Automatically transcribes speech from any video

🕒 Generates .srt subtitle files with accurate timestamps

📦 Uses Whisper models (tiny, base, small, medium, large, etc.)

📝 Easy to use with minimal setup

📦 Requirements

Before running the tool, make sure you have the following installed:

Python 3.7+

pip

Whisper dependencies:

pip install git+https://github.com/openai/whisper.git

Optional but recommended: FFmpeg for better audio extraction

📥 Installation

Clone the repository:

git clone https://github.com/KDurgaPrasad116/Auto-Subtitle-Generator.git
cd Auto-Subtitle-Generator

Install required packages (example):

pip install -r requirements.txt

If you don’t have requirements.txt, just install Whisper and any missing dependencies manually.

📖 Usage

Update variables in the script or run it directly:

python main.py

By default, it runs on:

video_file = "sample_video.mp4"
subtitle_file = "output_subtitles.srt"

To customize:

Replace "sample_video.mp4" with your own video path

Optional: change the Whisper model used (tiny, base, small, etc.)

Run the script to generate the subtitle file

🛠️ How It Works

The script loads a Whisper transcription model and:

Reads the input video

Transcribes the audio into text segments

Formats each segment into .srt with timestamps

Writes them to output_subtitles.srt

Example snippet from the transcribing logic:

model = whisper.load_model(model_size)
result = model.transcribe(video_path)
segments = result['segments']

The formatted timestamps follow the .srt format:

00:00:12,345 --> 00:00:15,678
Subtitle text here
🧪 Sample Files

Included in this repository:

📹 sample_video.mp4 — Example video

📝 output_subtitles.srt — Resulting subtitle file

These help you test the script quickly and see how subtitles are generated.

⚙️ Customization

You can adapt the tool to:

Use different Whisper model sizes

Add CLI parameters

Integrate with a video processing pipeline

Convert to embedded subtitles using FFmpeg

❤️ Contributing

Contributions are welcome!

Suggestions:

Add support for other audio sources

Provide command-line flags

Export subtitles in different formats (e.g., .vtt)

Add support for embedding subtitles into the video

If you want, I can also generate a detailed usage CLI wrapper or update the script to support arguments like:

python main.py --input myvideo.mp4 --output subs.srt --model medium

Just ask!
