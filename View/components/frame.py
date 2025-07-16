import tkinter as tk

class frame():

    def __init__(self):
        self._root = tk.Tk()
        self._defaultResizable()
    
    def setSize(self, width: int, height: int):
        self._root.geometry(f"{width}x{height}")
        return self
    
    def setTitle(self, title: str):
        self._root.title(title)
        return self
    
    def _defaultResizable(self):
        self._root.resizable(width = False, height = False)
        return self
    
    def setBackground(self, color: str):
        self._root.configure(bg = color)
        
    def getRoot(self):
        return self._root
    
    def show(self):
        self._root.mainloop()
