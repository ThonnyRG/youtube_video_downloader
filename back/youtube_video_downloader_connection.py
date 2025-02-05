import yt_dlp


ytlink = input("Insert link video: \n")
opts = {'outtmpl': "/Users/macbook/Downloads/%(title)s.mp4", 'format' : 'best',}

print("Downloading...")
try:
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([ytlink])
    print("DOWNLOADED")
except Exception as e:
    print(f"Error: {e}")
