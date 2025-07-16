from View.components.frame import frame


class FrameWhite(frame):
   
   def __init__(self):
      super().__init__()
      self._setupFrameWhite()
   
   def _setupFrameWhite(self):
      (self.setSize(500, 500).
      setTitle("python is trash")
      .setBackground("#222222"))
   # defaultFolder = "Users/macbook/Downloads"

   # labelTitle = tk.Label(root, text = "Video media downloader", font="Roboto 24 bold", bg= "#222222")
   # labelTitle.place(x = 100, y = 40)

   # labelSubtitle = tk.Label(root, text = "Enter in this box the full URL of your video:", font="Roboto 20", bg= "#222222") 
   # labelSubtitle.place(x = 70, y = 100)

   # labelSave = tk.Label(root, text = "Save to:", font="Roboto 20", bg= "#222222") 
   # labelSave.place(x = 210, y = 140)

   # folderTextbox = ctk.CTkEntry(root,textvariable = tk.StringVar(root,defaultFolder) ,height= 46, width=327, state = tk.DISABLED, font=("roboto",22), text_color = "#9AA0A6")
   # folderTextbox.place( x = 30, y = 172)
   # sc = folderTextbox.get()

   # entrylabel = ctk.CTkEntry(root, placeholder_text="ENTER URL VIDEO",height= 45, width=450, font=("roboto",22), text_color = "#9AA0A6")
   # entrylabel.place( x = 30, y = 237)
   # inputUrl = entrylabel.get()

   # browseButton = mtk.Button(root, text = "Browse", font = "Roboto 20", fg = "#ffffff", bg = "#4285F4", height= 47,width=98,  borderless = 1,activebackground="#315b9e")
   # browseButton.place(x = 384, y = 170)
 
   # clearButton = mtk.Button(root, text = "Clear",font = "Roboto 20",fg = "#174EA6", bg = "#222222", borderless = 1, activebackground="#222222", activeforeground = "#174EA6")
   # clearButton.place(x = 30, y = 300) 
 
   # pasteButton = mtk.Button(root, text = "Paste",font = "Roboto 20" , borderless = 1, fg = "#174EA6", bg = "#222222", activebackground="#222222", activeforeground = "#174EA6")
   # pasteButton.place(x = 195, y = 300) 
  
   # folderTextbox = mtk.Button(root, text = "Download",font = "Roboto 20" , fg = "#4285F4", bg = "#D2E3FC", state =tk.DISABLED)
   # folderTextbox.place(x = 350, y = 300) 

   # def validateURL(UrlVideo):
   #    r = requests.get(UrlVideo)
   #    "Video unavailable" in r.text
   
   # verifyingUrl = validateURL(inputUrl)
   
   # def buttonLink(option):
   #    if option:
   #       a = AlertFrame("Not valid url video")
   #       a.mainLoop()
         
   # root.mainloop()