import os
import tkinter as tk
from tkinter import filedialog
import platform

class fileDownloader:
    
    def selectFolder(self, saveFolder: str):
        try:
            root = tk.Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            
            folder_path = filedialog.askdirectory(
                title = "Select the folder where you can save the video",
                initialdir = saveFolder
            )
            
            root.destroy()
            
            if folder_path:
                return folder_path
            else:
                return None
        except Exception as e:
            return saveFolder
            
    def getDefaultFolder(self):
        operatingSystem = platform.system()
        
        if operatingSystem == "Windows":
            return os.path.join(os.path.expanduser("~"), "Downloads")
        elif operatingSystem == "Darwin":
            return os.path.join(os.path.expanduser("~"), "Downloads")