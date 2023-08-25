# music player with tkinter
# discord status integration

import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        pygame.init()
        pygame.mixer.init()

        self.track = tk.StringVar()
        self.status = tk.StringVar()
        
        

        # Create the GUI layout

        # Frame for Track & status label
        trackframe = tk.LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        trackframe.grid(row=0, column=0, sticky='nsew')


        songtrack = tk.Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"), bg="grey", fg="navyblue")
        songtrack.grid(row=0, column=1, padx=10, pady=5)

        trackstatus = tk.Label(trackframe, textvariable=self.status, font=("times new roman", 24, "bold"), bg="grey", fg="navyblue")
        trackstatus.grid(row=0, column=2, padx=10, pady=5)

        # Buttons Frame
        buttonframe = tk.LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        buttonframe.grid(row=1, column=0, sticky='nsew')

        # Play button
        playbtn = tk.Button(buttonframe, text="PLAY", command=self.play_song, width=10, font=("times new roman", 16, "bold"), bg="navyblue", fg="white")
        playbtn.grid(row=0, column=0, padx=10, pady=5)

        # Pause button
        playbtn = tk.Button(buttonframe, text="PAUSE", command=self.pause_song, width=10, font=("times new roman", 16, "bold"), bg="navyblue", fg="white")
        playbtn.grid(row=0, column=1, padx=10, pady=5)

        # Unpause button
        playbtn = tk.Button(buttonframe, text="UNPAUSE", command=self.unpause_song, width=10, font=("times new roman", 16, "bold"), bg="navyblue", fg="white")
        playbtn.grid(row=0, column=2, padx=10, pady=5)

        # Playlist Frame
        songsframe = tk.LabelFrame(self.root, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        songsframe.grid(row=0, column=1, rowspan=2, sticky='nsew')

        self.root.grid_rowconfigure(0, weight=1)  # Allow the top row to expand
        self.root.grid_rowconfigure(1, weight=1)  # Allow the bottom row to expand
        self.root.grid_columnconfigure(0, weight=1)  # Allow the left column to expand
        self.root.grid_columnconfigure(1, weight=2)  # Allow the right column (playlist) to expand more

        # Scrolling bar
        scrol_y = tk.Scrollbar(songsframe, orient=tk.VERTICAL)
        self.playlist = tk.Listbox(songsframe, yscrollcommand=scrol_y.set, font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", selectbackground="gold", selectmode=tk.SINGLE)
        scrol_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlistbox = self.playlist
        self.playlist.pack(fill=tk.BOTH)

        # Changing directory for fetching songs
        os.chdir("musicFiles")

        # Fetching songs
        songtracks = [track for track in os.listdir() if not track.startswith('.') and track.endswith('.mp3')]

        # Inserting songs into playlist
        for track in songtracks:
            self.playlist.insert(tk.END, track)

        self.playlist.bind("<Double-1>", self.play_song)

    def play_song(self, event=None):
        self.track.set(self.playlist.get(tk.ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(tk.ACTIVE))
        pygame.mixer.music.play()

    def pause_song(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpause_song(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x200+200+200")
    root.resizable(True, True)  # Allow window to be resizable
    MusicPlayer(root)
    root.mainloop()
