import yt_dlp

class mediaDownloader():
    
    def __init__(Self, LinkVideo, SaveFolder):
        Self.LinkVideo = LinkVideo
        Self.SaveFolder = SaveFolder
        
                
            
    def setLinkMedia(self):
        folder = self.SaveFolder
        format = folder+"%(title)s.mp4"
        linkMedia = self.LinkVideo
        
        opts = {'outtmpl': format, 'format' : 'best',}
        
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([linkMedia])
                print("downloading")
        except Exception as e:
            print(f"Error: {e}")
