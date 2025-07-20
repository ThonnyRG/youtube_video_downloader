from View.components.label import label


class titleLabel(label):
    def __init__(self, frame, text: str, x : int, y : int):
        self._text = text
        self._x = x
        self._y = y
        super().__init__(frame)
        self._setPosition()
        self._setupLabel()
        
    def _setupLabel(self):
        (self.setText(self._text).
         setFont("Roboto 24 bold").
         setBackground("#222222")
         )

    def _setPosition(self):
        self._label.place(x = self._x, y = self._y)    
    