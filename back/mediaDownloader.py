import yt_dlp

class mediaDownloader():
    
    def __init__(Self, LinkVideo, SaveFolder):
        Self.LinkVideo = LinkVideo
        Self.SaveFolder = SaveFolder
       
                
    def _getOptions(self):
        format = self.SaveFolder+"%(title)s.mp4"
        return{'outtmpl': format, 'format' : 'best',}
    
    def downloadMedia(self):
        try:
            opts = self._getOptions()
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([self.LinkVideo])
                return "downloading"
        except Exception as e:
            return f"Error: {str(e)}"
