import os
import subprocess
from tkinter import Tk, ttk, StringVar, Toplevel, Label, Button, Frame
from tkinter.constants import END
from social_media_downloader import SocialMediaDownloader
import tkinter as tk
from tkinter.font import Font

class AIOMediaTool:
    def __init__(self, master):
        self.master = master
        master.title("Social Download Media - Tool Lỏ")
        master.geometry("580x280")
        master.resizable(False, False)
        master.configure(bg="#f5f5f5")

        # Set the application icon
        try:
            self.master.iconbitmap(os.path.join(sys.path[0], 'icon.ico'))
        except:
            print("Failed to set application icon.")

        self.social_media_downloader = SocialMediaDownloader(self.master, self)

        # Status Bar
        self.status_bar_font = Font(family="Montserrat", size=12)
        self.status_bar = ttk.Label(master, text="", anchor="w", style="CustomStatusBar.TLabel")
        self.status_bar.pack(side="bottom", fill="x", padx=20, pady=10)
        self.status_bar.config(font=self.status_bar_font)
        self.status_bar.configure(background="#f5f5f5")


        # Version Label
        self.version_label = ttk.Label(master, text="Version 2.3.3 @ vuthao.id.vn", anchor="e", style="CustomVersionLabel.TLabel")
        self.version_label.pack(side="bottom", fill="x", padx=10, pady=0)
        self.version_label.configure(background="#f5f5f5")



root = Tk()
app = AIOMediaTool(root)
root.mainloop()
