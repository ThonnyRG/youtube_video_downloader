from View.components.frame import frame

class frameAlert(frame):
    def __init__(self):
        super().__init__()
        self._setupFrame()
        
    def _setupFrame(self):
        (self.setSize(500, 200)
         .setTitle("Message")
         .setBackground("#222222"))
       
    def closeWindow(self):
        self._root.destroy()