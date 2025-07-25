import yt_dlp
import os

class mediaDownloader():
    
    def __init__(Self, LinkVideo, SaveFolder):
        Self.LinkVideo = LinkVideo
        Self.SaveFolder = SaveFolder
        
    def progress_hook(self, d):
        """Hook para mostrar progreso de descarga"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            print(f"Downloading... {percent} at {speed}")
        elif d['status'] == 'finished':
            print(f"Download completed: {d['filename']}")
               
    def _getOptions(self):
        save_path = self.SaveFolder
        if not save_path.endswith(os.sep):
            save_path += os.sep
            
        format = self.SaveFolder + "/" + "%(title)s.mp4"
        return{'outtmpl': format, 'format' : 'best',}
    
    def downloadMedia(self):
        try:
            opts = self._getOptions()
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([self.LinkVideo])
                return "downloaded!!"
        except Exception as e:
            return f"Error: {str(e)}"
