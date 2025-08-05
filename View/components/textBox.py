import customtkinter as ctk

class textBox():
    def __init__(self, frame):
        self._textBox = ctk.CTkEntry(frame)
        
    def setText(self, message: str):
        self._textBox.configure(placeholder_text = message)
        return self
        
    def setFont(self, font : str, size: int):
        self._textBox.configure(font =(font, size))
        return self
    
    def setColor(self, color: str):
        self._textBox.configure(text_color = color)
        return self
    
    def setSize(self, h : int, w : int):
        self._textBox.configure(height = h, width = w)
        return self
        
    def getText(self):
        return self._textBox.get()
    
    def clearText(self):
        self._textBox.delete(0, "end")
        return self
    
    def insertText(self, content: str):
        self.clearText()
        self._textBox.insert(0, content)
        return self
           
    def setPosition(self, x: int, y : int):
        self._textBox.pack(padx = x, pady = y)
        