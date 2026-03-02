import whisper
from datetime import timedelta
import os

def format_timestamp(seconds):
    """
    TO get the time stamp of the input video in format : HH:MM:SS,mmm
    """
    td = timedelta(seconds=seconds)
    hours,remainder = divmod(td.seconds,3600)
    minutes,secs = divmod(remainder,60)
    milliseconds = int(td.microseconds / 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"

def generate_srt(video_path, output_srt_path, model_size="base"):
    """
    Transcribe the input video and generate the output as SRT subtitle file
    :video_path : input video path
    :output_srt_path : output srt subtitle file path
    """
    if not os.path.exists(video_path):
        print(f"Error: Could not find video file at {video_path} ")
        return

    print(f"Loading Whisper '{model_size}' model...")
    #models range from : tiny, base, small, medium, large
    model = whisper.load_model(model_size)

    print(f"Transcribing '{video_path}'... This might take a moment.")
    #Transcribing the audio from the video might take the cpu/gpu performance!!!

    result = model.transcribe(video_path)
    segments = result['segments']

    print("Generating SRT file...")

    with open(output_srt_path,"w",encoding="utf-8") as srt_file:
        for i, segments in enumerate(segments,start =1):
            # Extract start and end times
            start_time =format_timestamp(segments['start'])
            end_time = format_timestamp(segments['end'])
            text = segments['text'].strip()

            # Write in standard SRT format
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{text}\n\n")

    print(f"Success! Subtitles saved to : {output_srt_path}")

if __name__ == "__main__":
    """
    # Place the Video to be used as input in the same folder as this script to reduce confusion
    """
    video_file = "sample_video.mp4"
    subtitle_file = "output_subtitles.srt"

    generate_srt(video_file,subtitle_file)