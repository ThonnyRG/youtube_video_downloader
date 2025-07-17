import tkinter as tk 

class label():
    def __init__(self, frame):
        self._label = tk.Label(frame)
       
    def setText(self, message: str):
        self._label.config(text = message)
        return self
    
    def setFont(self, customFont: str):
        self._label.config(font = customFont)
        return self
        
    def setPosition(self, xPlace: int, yPlace: int):
        self._label.place(x = xPlace, y = yPlace)
        return self
        
    def setBackground(self, background : str):
        self._label.config(bg = background)
        return self
    
    def getLabel(self):
        return self._label