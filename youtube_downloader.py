import yt_dlp
import os

# -------- Progress Function --------

def progress(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']}", end="")
    elif d['status'] == 'finished':
        print("\nDownload complete! Merging audio and video...")


# -------- Inputs --------

url = input("Enter YouTube video URL: ")
folder = input("Enter folder path to save video: ")

print("\nSelect Video Quality:")
print("1. 720p")
print("2. 1080p")
print("3. Best Available")

choice = input("Enter choice (1/2/3): ")


# -------- SAFE Format Selection --------

if choice == "1":
    video_format = "bestvideo[height<=720]+bestaudio"
elif choice == "2":
    video_format = "bestvideo[height<=1080]+bestaudio"
else:
    video_format = "bestvideo+bestaudio"

try:
    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_opts = {
        'format': video_format,
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [progress],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Hurray! Video saved successfully ")

except Exception as e:
    print("\nError:", e)
