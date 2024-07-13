import yt_dlp
from moviepy.editor import *

def downlad_video(url, output_path="./output/video.mp4"):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Downloading video to {output_path}")
    return output_path

def convert_mp4_to_mp3(input_path, output_path="./output/audio.mp3"):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)
    print(f"Converting mp4 to mp3 and saving to {output_path}")
    return output_path

print("Welcome to Youtube Downloader")
url = input("Enter the URL of the video: ")
file_name = input("Enter the name of the file to save the video and audio: ")
output_video = "./output/" + file_name + ".mp4"
output_audio = "./output/" + file_name + ".mp3"
downlad_video(url, output_video)
convert_mp4_to_mp3(output_video, output_audio)
print("Done!")