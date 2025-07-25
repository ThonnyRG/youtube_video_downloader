from View.components.label import label


class subtitleLabel(label):
    def __init__(self, frame, text: str, x : int, y : int):
        self._text = text
        self._x = x
        self._y = y
        
        super().__init__(frame)
        self._setupLabel()
        self._setAlignment()
        self._setFontColor()
        self._setPosition()

        
    def _setupLabel(self):
        (self.setText(self._text).
         setFont("Roboto 22")
         .setBackground("#222222")
         )
        
    def _setPosition(self):
        self._label.pack(padx = self._x, pady = self._y)
       
    def _setFontColor(self):
        self._label.config(fg = "#9AA0A6")
        return self
        
    def _setAlignment(self):
        self._label.config(anchor = "w", justify = "left")
        return self
    
    def setWrap(self, warp : int):
        self._label.config(wraplength = warp)