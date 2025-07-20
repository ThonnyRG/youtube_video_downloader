from View.components.label import label
from tkinter import font

class underlineLabel(label):
    def __init__(self, frame, text: str, x : int, y : int, cmd):
        self._text = text
        self._x = x
        self._y = y
        self._cmd = cmd
        self._font = font.Font(family = "Roboto", size = 24, underline = True)
        
        super().__init__(frame)
       
        self._addAcion()
        self._setPosition()
        self._setForeground()
        self._setupLabel()
        
    def _setupLabel(self):
        (self.setText(self._text).
         setFont(self._font).
         setBackground("#222222")
         )
        
    def _setPosition(self):
        self._label.place(x = self._x, y = self._y)    
    
    def _addAcion(self):
        self._label.pack()
        self._label.bind('<Button-1>', self._cmd)
        
    def _setForeground(self):
        self._label.config(fg = "#4285F4")
        