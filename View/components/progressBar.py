from tkinter import ttk

class progresBar:
    def __init__(self, frame):
        self._frame = frame
        self._barr = ttk.Progressbar(frame, mode = "indeterminate")
        self._setupProgressBar()
    
    def _setupProgressBar(self):
        self._barr.place(x = 50, y = 100, width = 400)
        return self
    
    def startProcess(self):
        self._barr.start()
        return self
    
    def stopProcess(self):
        self._barr.stop()
        return self