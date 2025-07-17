from View.components.frame import frame


class frameAlert(frame):
    def __init__(self):
        super().__init__()
        self._setupFrame()
        
    def _setupFrame(self):
        (self.setSize(500, 200)
         .setTitle("Atention!")
         .setBackground("#222222"))