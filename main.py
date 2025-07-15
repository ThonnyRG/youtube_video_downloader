# from UI.AlertFrame import AlertFrame
from back.mediaDownloader import mediaDownloader

def main():
    # a = AlertFrame("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
    # a.setAlert()
    link = "https://www.instagram.com/reel/DFI-yZTyb9i/?utm_source=ig_web_copy_link"
    folder = "/Users/macbook/Downloads/"
    a = mediaDownloader(link, folder)
    r = a.downloadMedia()
    print(r)
if __name__=="__main__":
    main()
