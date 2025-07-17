from View.components.button import button


class clearButton(button):
    def __init__(self, frame, message : int, action, x: int, y :int):
        self._x = x
        self._y = y
        self._message = message
        self._action = action
        super().__init__(frame)
        self._setupButton()
        
    def _setupButton(self):
        (self.setText(self._message).
         setBackgroud("#222222","#222222").
         setForeGround("#174EA6","#174EA6").
         setPlace(self._x, self._y).
         setAction(self._action).
         setSize().
         setBorderless()
        )