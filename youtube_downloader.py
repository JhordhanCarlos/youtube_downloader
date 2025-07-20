import sys
import os
from yt_dlp import YoutubeDL
import ffmpeg
from dotenv import load_dotenv

def get_ffmpeg_path():
    load_dotenv()
    ffmpeg_path = os.getenv('FFMPEG_PATH')
    if not ffmpeg_path:
        print('FFMPEG path not found in .env. Please add FFMPEG_PATH to your .env file.')
        sys.exit(1)
    return ffmpeg_path

def download_youtube_video(link):
    ffmpeg_path = get_ffmpeg_path()
    print('Downloading video and audio with yt-dlp (library)...')
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio[ext=m4a]',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'ffmpeg_location': ffmpeg_path
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    # Check for separate video and audio files
    files = os.listdir()
    mp4s = [f for f in files if f.endswith('.mp4')]
    m4as = [f for f in files if f.endswith('.m4a')]

    # If both .mp4 and .m4a exist, merge with ffmpeg-python
    if mp4s and m4as:
        video_file = mp4s[0]
        audio_file = m4as[0]
        output_file = video_file.replace('.mp4', '_final.mp4')
        print(f'Merging {video_file} + {audio_file} into {output_file}...')
        (
            ffmpeg
            .input(video_file)
            .input(audio_file)
            .output(output_file, vcodec='copy', acodec='aac', strict='experimental')
            .run(overwrite_output=True, cmd=ffmpeg_path)
        )
        print('Final video created:', output_file)
        # Remove separate files
        try:
            os.remove(video_file)
            os.remove(audio_file)
            print(f'Removed files {video_file} and {audio_file}.')
        except Exception as e:
            print(f'Error removing files: {e}')
    else:
        print('Download complete! (File already merged)')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python youtube_downloader.py <youtube_video_url>')
        sys.exit(1)
    link = sys.argv[1]
    download_youtube_video(link)
