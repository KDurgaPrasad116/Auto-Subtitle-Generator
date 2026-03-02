Here is your complete `README.md` file content:

# 📽️ Auto-Subtitle-Generator

A simple Python tool to automatically generate subtitle (`.srt`) files from video files using OpenAI Whisper.

This project transcribes the audio from a video file and converts it into a properly formatted `.srt` subtitle file with timestamps.

---

## 📑 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## 📖 Introduction

Auto-Subtitle-Generator uses OpenAI's Whisper speech recognition model to transcribe video audio into text and automatically generate subtitle files in `.srt` format.

It is designed to be simple, lightweight, and easy to use.

---

## 🚀 Features

- 🎤 Automatic speech recognition from video files
- 🕒 Generates accurate timestamped `.srt` subtitles
- 📦 Supports multiple Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`)
- 📝 Easy-to-modify Python script
- 🎬 Works with most video formats (requires FFmpeg)

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/KDurgaPrasad116/Auto-Subtitle-Generator.git
cd Auto-Subtitle-Generator
````

### 2️⃣ Install Dependencies

Install Whisper directly:

```bash
pip install git+https://github.com/openai/whisper.git
```

Or install using requirements (if available):

```bash
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg (Recommended)

Whisper requires FFmpeg for audio extraction.

* Windows: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
* Mac:

```bash
brew install ffmpeg
```

* Ubuntu:

```bash
sudo apt install ffmpeg
```

---

## ▶️ Usage

1. Open the Python script.
2. Set your video file path:

```python
video_file = "sample_video.mp4"
subtitle_file = "output_subtitles.srt"
model_size = "base"
```

3. Run the script:

```bash
python main.py
```

4. The generated subtitles will be saved as:

```
output_subtitles.srt
```

---

## ⚙️ Configuration

You can modify:

| Variable        | Description              |
| --------------- | ------------------------ |
| `video_file`    | Path to input video      |
| `subtitle_file` | Output subtitle filename |
| `model_size`    | Whisper model size       |

### Available Model Sizes

* `tiny` (Fastest, least accurate)
* `base`
* `small`
* `medium`
* `large` (Most accurate, slower)

---

## 📄 Example Output (.srt format)

```
1
00:00:01,200 --> 00:00:03,500
Hello and welcome.

2
00:00:04,000 --> 00:00:06,800
This is an example subtitle.
```

---

## 🧪 Example Files

* `sample_video.mp4` – Sample input video
* `output_subtitles.srt` – Generated subtitle file

---

## ❗ Troubleshooting

### Whisper not installing?

Upgrade pip first:

```bash
pip install --upgrade pip
```

### FFmpeg not found?

Make sure FFmpeg is installed and added to your system PATH.

### CUDA/GPU Issues?

If using GPU acceleration, ensure:

* Correct CUDA version installed
* Compatible PyTorch version

---

## 👥 Contributors

* Project Author: KDurgaPrasad116

Contributions are welcome! Feel free to fork and submit pull requests.

---

## 📜 License

This project currently does not include a license file.

It is recommended to add an MIT License or another open-source license for clarity.

---

## 💡 Future Improvements

* Add CLI argument support
* Add support for `.vtt` format
* Add batch video processing
* Embed subtitles directly into videos
* Build a simple GUI interface

---

⭐ If you found this project useful, consider giving it a star!

```

If you'd like, I can also generate:
- A **professional GitHub-optimized version**
- A **CLI-based version README**
- Or a **more advanced production-ready README**

Just tell me which style you prefer.
```
