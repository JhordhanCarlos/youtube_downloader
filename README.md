# YouTube Downloader

A simple Python script to download YouTube videos in Full HD (1080p) and automatically merge separate video and audio files into a single MP4 file using yt-dlp and ffmpeg.

## Features

- Downloads YouTube videos in the best available 1080p quality
- Merges video and audio automatically
- Keeps the original video name
- Removes temporary files after merging
- Portable: ffmpeg path is set via `.env` file

## Requirements

- Python 3.7+
- yt-dlp (`pip install yt-dlp`)
- ffmpeg-python (`pip install ffmpeg-python`)
- python-dotenv (`pip install python-dotenv`)
- ffmpeg executable (download from https://ffmpeg.org/download.html)

## Setup

1. Clone or download this repository.
2. Install the required Python packages:
   ```
   pip install yt-dlp ffmpeg-python python-dotenv
   ```
3. Download ffmpeg and extract it to a folder of your choice.
4. Copy `.env-example` to `.env` and set the path to your `ffmpeg.exe`:
   ```
   FFMPEG_PATH=C:/path/to/ffmpeg.exe
   ```
   (Use `/` or `\\` for the path)

## Usage

Run the script from the command line:

```
python youtube_downloader.py "<youtube_video_url>"
```

The final merged video will be saved in the current directory with the original YouTube title.

## Example

```
python youtube_downloader.py "https://www.youtube.com/watch?v=example"
```

## Notes

- If the video and audio are downloaded separately, the script will merge them and remove the temporary files.
- Make sure the ffmpeg path in `.env` is correct and points to the actual `ffmpeg.exe` file.
