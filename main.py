'''
USAGE - The program is a Python script that downloads the audio of a YouTube 
        video from a given link and converts it to MP3 format using the pytube 
        and pydub libraries. The downloaded audio file is saved to a directory 
        specified by the DOWNLOAD_DIR variable, and the converted MP3 file is 
        saved with the same name as the original file but with the .mp3 extension. 
        The program disables SSL verification to allow downloading YouTube videos 
        and prompts the user to enter a YouTube video link. Finally, the program 
        prints a success message with the path to the converted MP3 file.

AUTHOR - https://github.com/Ahendrix9624
'''

import pytube
import ssl
from pydub import AudioSegment

DOWNLOAD_DIR = 'downloads/'
AUDIO_EXTENSION = '.mp3'

def disable_ssl_verification():
    """Disables SSL verification to allow downloading YouTube videos."""
    ssl._create_default_https_context = ssl._create_unverified_context

def download_audio(video_url):
    """Downloads the audio of a YouTube video and saves it to disk."""
    # Create a YouTube object and extract the audio stream
    yt = pytube.YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream
    print("Downloading audio...")
    audio_file = audio_stream.download(DOWNLOAD_DIR)

    return audio_file

def convert_audio_to_mp3(audio_file):
    """Converts the downloaded audio file to MP3 format using pydub."""
    print("Converting audio to MP3...")
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)

    # Set the output file name
    mp3_file = audio_file.replace('.webm', AUDIO_EXTENSION)

    # Export the audio to MP3 format
    audio.export(mp3_file, format='mp3')

    return mp3_file

def main():
    """Main function that runs the program."""
    disable_ssl_verification()

    # Prompt the user to enter a YouTube video link
    video_url = input("Enter the YouTube video link: ")

    # Download the audio and convert it to MP3
    audio_file = download_audio(video_url)
    mp3_file = convert_audio_to_mp3(audio_file)

    print(f"Audio downloaded and converted successfully! Saved to {mp3_file}")

if __name__ == '__main__':
    main()
