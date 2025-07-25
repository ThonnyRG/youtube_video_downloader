from View.components.label import label
from tkinter import font

class underlineLabel(label):
    def __init__(self, frame, text: str, x : int, y : int, cmd, underline: bool):
        self._text = text
        self._x = x
        self._y = y
        self._cmd = cmd
        self._underline = underline
        
        super().__init__(frame)
       
        self._addAcion()
        self._setPosition()
        self._setForeground()
        self._setupLabel()
        self._setUnderline()
        
    def _setupLabel(self):
        (self.setText(self._text).
         setBackground("#222222")
         )
        
    def _setPosition(self):
        self._label.pack(padx = self._x, pady = self._y)    
    
    def _addAcion(self):
        self._label.pack()
        self._label.bind('<Button-1>', self._cmd)
        
    def _setForeground(self):
        self._label.config(fg = "#4285F4")
        
    def _setUnderline(self):
        self._label.config(font = font.Font(family = "Roboto", size = 24, underline = self._underline))
        
    
        