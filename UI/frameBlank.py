import tkinter as tk
from tkinter import ttk


class FrameWhite():
   root = tk.Tk()
  
   
  
   root.geometry("500x500")
   root.title("Media downloader")
   root.resizable(width = False,height = False)
   root.config(bg = "#222222")
      
   labelTitle = tk.Label(root, text = "Video media downloader", font="Roboto 24 bold", bg= "#222222")
   labelTitle.place(x = 100, y = 40)
 
   labelSubtitle = tk.Label(root, text = "Enter in this box the full URL of your video:", font="Roboto 20", bg= "#222222") 
   labelSubtitle.place(x = 50, y = 100)

   labelSave = tk.Label(root, text = "Save to:", font="Roboto 20", bg= "#222222") 
   labelSave.place(x = 80, y = 140)


   downloadButton = tk.Button(root, text = "C:Users/downloads",font = "Roboto 20" , fg = "#4285F4", bd = 0, highlightbackground = '#222222')
   downloadButton.place( x = 160, y = 137)

   
   
   clearButton = tk.Button(root, text = "Clear",font = "Roboto 20" , fg = "#174EA6", bd = 0, bg = "#174EA6")
   clearButton.place(x = 50, y = 250) 
  
   pasteButton = tk.Button(root, text = "Paste",font = "Roboto 20" , fg = "#174EA6", bd = 0, bg = "#174EA6")
   pasteButton.place(x = 200, y = 250) 
  
   downloadButton = tk.Button(root, text = "Download",font = "Roboto 20" , fg = "#4285F4", bd = 0, bg = "#4E4E4E")
   downloadButton.place(x = 330, y = 250) 
  
   root.mainloop()
     