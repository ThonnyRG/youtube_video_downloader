import tkinter as tk
import customtkinter as ctk 
import tkmacosx as mtk

class FrameWhite():
   root = tk.Tk()
  
   root.geometry("500x500")
   root.title("Media downloader")
   root.resizable(width = False,height = False)
   root.config(bg = "#222222")
      
   labelTitle = tk.Label(root, text = "Video media downloader", font="Roboto 24 bold", bg= "#222222")
   labelTitle.place(x = 100, y = 40)
 
   labelSubtitle = tk.Label(root, text = "Enter in this box the full URL of your video:", font="Roboto 20", bg= "#222222") 
   labelSubtitle.place(x = 70, y = 100)

   labelSave = tk.Label(root, text = "Save to:", font="Roboto 20", bg= "#222222") 
   labelSave.place(x = 210, y = 140)

   downloadButton = ctk.CTkEntry(root,placeholder_text = "Users/macbook/Downloads" ,height= 40, width=320)
   downloadButton.place( x = 50, y = 175)

   entrylabel = ctk.CTkEntry(root, placeholder_text="ENTER URL VIDEO",height= 40, width=400)
   entrylabel.place( x = 50, y = 237)
  
   browseButton = mtk.Button(root, text = "Browse", font = "Roboto 20", fg = "#174EA6", bd = 0, bg = "#222222")
   browseButton.place(x = 355, y = 175)
   
   clearButton = mtk.Button(root, text = "Clear",font = "Roboto 20" , fg = "#174EA6", bd = 0, bg = "#222222")
   clearButton.place(x = 50, y = 300) 
  
   pasteButton = mtk.Button(root, text = "Paste",font = "Roboto 20" , fg = "#174EA6", bd = 0, bg = "#222222")
   pasteButton.place(x = 200, y = 300) 
  
   downloadButton = mtk.Button(root, text = "Download",font = "Roboto 20" , fg = "#4285F4", bd = 0, bg = "#4E4E4E")
   downloadButton.place(x = 330, y = 300) 
  
   root.mainloop()
     