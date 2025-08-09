import platform

class button():
    def __init__(self, frame):
        self._setOS()
        self._button = self.tk.Button(frame)
        self._setFont()
        
    def _setOS(self):
        operatingSystem = platform.system()
        
        if operatingSystem == "Darwin":
            try:
                import tkmacosx as tk
                self.tk = tk
            except: 
                import tkinter as tk
                self.tk = tk
        else:
            import tkinter as tk
            self.tk =tk
    
    def setText(self, message: str):
        self._button.config(text = message)
        return self
    
    def _setFont(self):
        self._button.config(font = "Roboto 20")
        return self
    
    def setForeGround(self, foreGround : str, activeForeGround: str):
        self._button.config(fg = foreGround,  activeforeground = activeForeGround)
        return self
       
    def setSize(self):
        self._button.config(padx = 10, pady = 10)
        return self
    
    def setBorderless(self):
        self._button.config(borderless = 1)
        return self
    
    def setBackgroud(self, background : str, activeBackground : str):
        self._button.config(bg = background,  activebackground = activeBackground)
        return self
   
    def setPlace(self, X : int, Y : int):
        self._button.place(x = X,y = Y)
        return self
    
    def setEnabled(self, answer : bool):
        if (answer != True):
            self._button.config(state = self.tk.DISABLED)
        else:
            self._button.config(state = self.tk.NORMAL)
        return self
    
    def setAction(self, cmd):
        self._button.configure(command = cmd)
        return self
        