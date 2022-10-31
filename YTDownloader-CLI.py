#!/usr/bin/python
from pytube import YouTube
from datetime import timedelta
import os
from moviepy.editor import *
# To do
# Some characters dont work when calling them with os.exists, os.remove, etc. ($)
# Get rid of filename_prefix?
# Catch wrong youtube link error

while True:
    url = input("Enter the youtube URL: ")
    yt = YouTube(url)
    # Info about the video
    print('----------Channel--------')
    print('Channel: ' + str(yt.author))
    print('Channel ID: ' + str(yt.channel_id))
    print('Channel URL: ' + str(yt.channel_url))
    print('Thumbnail: ' + str(yt.thumbnail_url))
    print('----------Media----------')
    print('Title: ' + str(yt.title))
    print('Date published: ' + str(yt.publish_date))
    print('Length: ' + "{:0>8}".format(str(timedelta(seconds=int(yt.length)))))
    print('Views: ' + str(yt.views))
    print('Age Restricted: ' + str(yt.age_restricted))
    # Video not available issue
    audio_err = '1Video Not Available.mp4'
    video_err = '2Video Not Available.mp4'
    error_found = 'The file failed to download. Retrying.....'
    # Download choices
    full_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/')  # Generic desktop path
    choice = input('[1]Audio/[2]Video/[3]Exit: ')

    if choice == '1':
        print('Downloading...')
        audio_download = YouTube(url).streams.get_audio_only().download(full_path, filename_prefix='1')
        # Checks if the file downloaded correctly
        if os.path.exists(full_path + '1' + str(yt.title) + '.mp4'):
            print('Audio file downloaded.' + '\n' + 'Converting to .mp3 format.....')
            convert_mp3 = AudioFileClip(full_path + '1' + str(yt.title) + '.mp4')     
            convert_mp3.write_audiofile(full_path + '1' + str(yt.title) + '.mp3')     
            convert_mp3.close()
            os.remove(full_path + '1' + str(yt.title) + '.mp4')
        elif os.path.exists(full_path + audio_err):
            os.remove(full_path + audio_err)
            print(error_found)
            audio_download
            print('Audio file downloaded.' + '\n')

    elif choice == '2':
        print('Downloading...')
        video_download = YouTube(url).streams.get_highest_resolution().download(full_path, filename_prefix='2')
        # Same ^^
        if os.path.exists(full_path + '2' + str(yt.title) + '.mp4'):
            print('Video file downloaded.' + '\n')
        elif os.path.exists(full_path + video_err):
            os.remove(full_path + video_err)
            print(error_found)
            video_download
            print('Video file downloaded.' + '\n')

    elif choice == '3':
        break
    else:
        print("Try again." + '\n')
