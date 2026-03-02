AI-Powered Auto Subtitle Generator
An automated pipeline to generate high-accuracy SubRip (.srt) subtitle files from local videos or YouTube links using OpenAI's Whisper model.

🚀 Overview
This project leverages state-of-the-art Speech-to-Text AI to eliminate the tedious work of manual transcription. By using a Transformer-based sequence-to-sequence model, it accurately identifies speech, handles technical jargon, and generates precise timestamps compatible with all major video players.

✨ Features
YouTube Integration: Provide a URL, and the script handles audio extraction via yt-dlp, transcription, and cleanup.

Local File Support: Process .mp4, .mkv, and other common video formats directly.

Intelligent Transcription: Powered by OpenAI Whisper, supporting multiple model sizes (tiny to large) to balance speed and accuracy.

Standardized Output: Generates industry-standard .srt files ready for use in VLC, YouTube, or Premiere Pro.

📺 Featured Sample
This project was tested and optimized using the following content:

Video: the FUN way to learn programming

Creator: crin

Result: Successfully transcribed technical concepts like negative indexing, string formatting, and API integration with high precision.

🛠️ Prerequisites
System Requirements
Python 3.7+

FFmpeg: Required for audio processing.

Windows: winget install ffmpeg

macOS: brew install ffmpeg

Linux: sudo apt install ffmpeg

Python Dependencies
Bash

pip install openai-whisper yt-dlp
📂 Project Structure
main.py: The core application logic.

output_subtitles.srt: Sample output generated from the AI model.

.gitignore: Configured to exclude heavy temporary audio and environment files.

🚀 Usage
Transcribing a YouTube Video
Update the yt_link in the script and run:

Python

yt_link = "https://youtu.be/kNareBFFWtQ?si=uKYdy1pf0Of_joi5"
generate_srt_from_youtube(yt_link, "output_subtitles.srt")
Transcribing a Local Video
Python

generate_srt("your_video.mp4", "output_subtitles.srt")
⚙️ Performance Tiers
Choose the right model size in whisper.load_model() based on your hardware:

base: Excellent for quick testing and clear audio.

small / medium: Recommended for technical tutorials to ensure acronyms and code terms are spelled correctly.

large: Best-in-class accuracy for complex audio (requires more VRAM/RAM).
