#!/usr/bin/python
import os
import sys
from time import sleep
from tkinter import *
from pytube import YouTube
from datetime import timedelta
from moviepy.editor import *
# To do
# Fix update bind button
# Some characters dont work when calling them with os.exists, os.remove, etc. ($#)

full_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/')  # Generic desktop path
# Video not available issue
audio_err = '1Video Not Available.mp4'
video_err = '2Video Not Available.mp4'

def audio():
    audio_download_file = yt.streams.get_audio_only().download(full_path, filename_prefix='1')
    # Checks if the file downloaded correctly
    if os.path.exists(full_path + audio_err):
            os.remove(full_path + audio_err)
            info_status.config(text='Status: Download failed. Retrying...')  
            root.update()
            sleep(1.6)
            audio_download_file # Retries to download the file
    else:
        info_status.config(text='Status: Converting to mp3...')  
        root.update() # Updates status message
        convert_mp3 = AudioFileClip(full_path + '1' + str(yt.title) + '.mp4')   
        convert_mp3.write_audiofile(full_path + '1' + str(yt.title) + '.mp3')
        convert_mp3.close()
        os.remove(full_path + '1' + str(yt.title) + '.mp4')
        info_status.config(text='Status: Audio file downloaded.')


def video():
    update()
    video_download_file = yt.streams.get_highest_resolution().download(full_path, filename_prefix='2')
    if os.path.exists(full_path + video_err):
            os.remove(full_path + video_err)
            info_status.config(text='Status: Download failed. Retrying...')  
            root.update()
            sleep(1.6)
            video_download_file # Retries to download the file
    info_status.config(text='Status: Video file downloaded.')


def update():
    global url, yt
    url = str(user_input.get())
    yt = YouTube(url)
    info_channel_id.config(text='ID: ' + str(yt.channel_id))
    info_channel.config(text='Channel: ' + str(yt.author))
    info_title.config(text='Title: ' + str(yt.title))
    info_views.config(text='Views: ' + str(yt.views))
    info_length.config(text='Length: ' + "{:0>8}".format(str(timedelta(seconds=int(yt.length)))))
    info_date.config(text='Date: ' + str(yt.publish_date))
    info_age.config(text='Age Restricted: ' + str(yt.age_restricted))
    info_status.config(text='Status: Downloading...')
    root.update()
    user_input.delete(0, END)


# Main window
root = Tk()
root.title('Youtube Downloader')
root.minsize(510, 230)
root.maxsize(510, 230)
program_directory = sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "among_youtube.png")))
photo = PhotoImage(file=os.path.join(program_directory, "youtube.png"))
logo = Label(image=photo) # image=photo
logo.place(x=355, y=106, height=130, width=155)

# User input for the URL
display_frame = Frame(root)
display_frame.place(x=8, y=10, height=30, width=500)
user_input = Entry(display_frame, font=("Helvetica", 12), bd=2, bg="white", width=5)
user_input.pack(expand=True, fill=BOTH)
user_input.bind("<KeyRelease>", update)

# Download options frame and labels
download_frame = LabelFrame(root, text="Download options")
download_frame.place(x=350, y=50, height=60, width=155)

download_video = Button(download_frame, text="Video", bd=1, highlightcolor="red", command=video)
download_video.grid(row=0, column=0, padx=8, pady=8)

download_audio = Button(download_frame, text="Audio", bd=1, highlightcolor="blue", command=audio)
download_audio.grid(row=0, column=1, padx=8)

# Video information frame and labels
info_frame = LabelFrame(root, text="Video information")
info_frame.place(x=8, y=50, height=170, width=340)

info_channel = Label(info_frame, text='Channel:')
info_channel.place(x=5, y=18)

info_channel_id = Label(info_frame, text='ID:')
info_channel_id.place(x=5, y=0)

info_title = Label(info_frame, text='Title:')
info_title.place(x=5, y= 36)

info_date = Label(info_frame, text='Date:')
info_date.place(x=5, y= 54)

info_length = Label(info_frame, text='Length:')
info_length.place(x=5, y= 72)

info_views = Label(info_frame, text='Views:')
info_views.place(x=5, y= 90)

info_age = Label(info_frame, text='Age Restricted:')
info_age.place(x=5, y= 108)

info_status = Label(info_frame, text='Status:')
info_status.place(x=5, y= 126)

root.mainloop()
