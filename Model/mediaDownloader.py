import yt_dlp
import os

class mediaDownloader():
    
    def __init__(Self, LinkVideo, SaveFolder):
        Self.LinkVideo = LinkVideo
        Self.SaveFolder = SaveFolder
               
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
                return "Video downloaded successfully!!"
        except Exception as e:
            return f"Error: {str(e)}"
