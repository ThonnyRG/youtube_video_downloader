import tkmacosx as tk

class button():
    def __init__(self, frame):
        self._button = tk.Button(frame)
        
    def setText(self, message: str):
        self._button.configure(text = message)
        return self
    
    def setFont(self, fontText: str):
        self._button.configure(font = fontText)
        return self
    
    def setForeGround(self, foreGround : str):
        self._button.configure(fg = foreGround,  activeforeground = foreGround)
        return self
       
    def setSize(self, h: int, w: int):
        self._button.configure(height = h, width = w)
        return self
    
    def setBorderless(self):
        self._button.configure(borderless = 1)
        return self
    
    def setBackgroud(self, background : str):
        self._button.configure(bg = background,  activebackground = background)
        return self
   
    def setPlace(self, X : int, Y : int):
        self._button.place(x = X,y = Y)
        return self
    
    def setEnabled(self, answer : bool):
        if (answer != True):
            self._button.configure(state = tk.DISABLED)
        return self
        
        
    
   # browseButton = mtk.Button(root, text = "Browse", font = "Roboto 20", fg = "#ffffff", bg = "#4285F4", height= 47,width=98,  borderless = 1,activebackground="#315b9e")
   # browseButton.place(x = 384, y = 170)
 
   # clearButton = mtk.Button(root, text = "Clear",font = "Roboto 20",fg = "#174EA6", bg = "#222222", borderless = 1, activebackground="#222222", activeforeground = "#174EA6")
   # clearButton.place(x = 30, y = 300) 
 
   # pasteButton = mtk.Button(root, text = "Paste",font = "Roboto 20" , borderless = 1, fg = "#174EA6", bg = "#222222", activebackground="#222222", activeforeground = "#174EA6")
   # pasteButton.place(x = 195, y = 300) 