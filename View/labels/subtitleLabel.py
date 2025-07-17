from View.components.label import label


class subtitleLabel(label):
    def __init__(self, frame, text: str, x : int, y : int):
        self._text = text
        self._x = x
        self._y = y
        super().__init__(frame)
        self._setupLabel()
        
    def _setupLabel(self):
        (self.setText(self._text).
         setFont("Roboto 22").
         setBackground("#9AA0A6").
         setPosition(self._x, self._y)
         )
    