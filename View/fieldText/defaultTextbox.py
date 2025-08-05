from View.components.textBox import textBox


class defaultTextBox(textBox):
    def __init__(self, frame, fieldText: str, x : int, y : int):
        self._x = x
        self._y = y
        self._fieldText = fieldText
        super().__init__(frame)
        self._setupTextBox()
        
    def _setupTextBox(self):
        (self.setText(self._fieldText).
        setColor("#FFFFFF").
        setFont("Roboto", 20).
        setSize(40, 400).
        setPosition(self._x ,self._y))