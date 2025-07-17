from View.components.frame import frame


class defaultFrame(frame):
    def __init__(self, frameName : str):
        self.frameName = frameName
        super().__init__()
        self._setupDefaultFrame()
        
    def _setupDefaultFrame(self):
        (self.setSize(500, 500).
         setTitle(self.frameName).
         setBackground("#222222"))
    