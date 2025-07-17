from View.components.button import button


class blueButton(button):
    def __init__(self, frame, message: str, action, x : int,y : int):
        self._x = x
        self._y = y
        self._message = message
        self._action = action
        super().__init__(frame)
        self._setupButton()
       
    def _setupButton(self):
        (self.setText(self._message).
         setBackgroud("#4285F4","#315b9e").
         setForeGround("#ffffff","#ffffff").
         setPlace(self._x, self._y).
         setAction(self._action).
         setSize().
         setBorderless()
        )
   