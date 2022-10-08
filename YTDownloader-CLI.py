#!/usr/bin/python

from pytube import YouTube
from datetime import timedelta


def yt_choice():
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
    # print('Length: ' + str("%.2f" % float(yt.length) / 60))
    print('Views: ' + str(yt.views))
    print('Age Restricted: ' + str(yt.age_restricted))
    # Download choices
    choice = input('[1]Audio/[2]Video/[3]Exit: ')
    if choice == '1':
        print('Downloading...')
        YouTube(url).streams.get_audio_only().download('/home/alex/Desktop/', filename_prefix='1')
        print('Audio downloaded.' + '\n')
    elif choice == '2':
        print('Downloading...')
        YouTube(url).streams.get_highest_resolution().download('/home/alex/Desktop/', filename_prefix='2')
        print('Video downloaded.' + '\n')
    elif choice == '3':
        return
    else:
        print("Try again." + '\n')
    yt_choice()


yt_choice()
