import os
import tkinter as tk
from tkinter import filedialog
import platform

class fileDownloader:
    def __init__(self):
        self._currentFolder = self.getDefaultFolder()
    
    def selectFolder(self):
        try:
            root = tk.Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            
            folder_path = filedialog.askdirectory(
                title="Select folder to save videos",
                initialdir=self._currentFolder
            )
            
            root.destroy()
            
            if folder_path:
                self._currentFolder = folder_path
                return folder_path
            else:
                # Si cancela, devolver la carpeta actual
                return self._currentFolder
        except Exception as e:
            return self._currentFolder
    
    def getCurrentFolder(self):
        return self._currentFolder
    
    def getDefaultFolder(self):
        operatingSystem = platform.system()
        
        if operatingSystem == "Windows":
            return os.path.join(os.path.expanduser("~"), "Downloads")
        elif operatingSystem == "Darwin":
            return os.path.join(os.path.expanduser("~"), "Downloads")
        else: 
            return os.path.join(os.path.expanduser("~"), "Downloads")