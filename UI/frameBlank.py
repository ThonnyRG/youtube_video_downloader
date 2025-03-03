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

   downloadButton = ctk.CTkEntry(root,textvariable = tk.StringVar(root,"Users/macbook/Downloads") ,height= 46, width=327, state = tk.DISABLED, font=("roboto",22), text_color = "#9AA0A6")
   downloadButton.place( x = 30, y = 172)

   entrylabel = ctk.CTkEntry(root, placeholder_text="ENTER URL VIDEO",height= 45, width=450, font=("roboto",22), text_color = "#9AA0A6")
   entrylabel.place( x = 30, y = 237)
  
   browseButton = mtk.Button(root, text = "Browse", font = "Roboto 20", fg = "#ffffff", bg = "#4285F4", height= 47,width=98,  borderless = 1,activebackground="#315b9e")
   browseButton.place(x = 384, y = 170)
  
   clearButton = mtk.Button(root, text = "Clear",font = "Roboto 20",fg = "#174EA6", bg = "#222222", borderless = 1, activebackground="#222222", activeforeground = "#174EA6")
   clearButton.place(x = 30, y = 300) 
 
   pasteButton = mtk.Button(root, text = "Paste",font = "Roboto 20" , borderless = 1, fg = "#174EA6", bg = "#222222", activebackground="#222222", activeforeground = "#174EA6")
   pasteButton.place(x = 195, y = 300) 
  
   downloadButton = mtk.Button(root, text = "Download",font = "Roboto 20" , fg = "#4285F4", bg = "#D2E3FC", state =tk.DISABLED)
   downloadButton.place(x = 350, y = 300) 
  
   root.mainloop()
     