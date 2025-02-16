

from back.mediaDownloader import mediaDownloader


def main():
    m = mediaDownloader("https://www.youtube.com/shorts/TJhWvEU_1_Y","/Users/macbook/Downloads/")
    m.setLinkMedia()
if __name__=="__main__":
    main()
  