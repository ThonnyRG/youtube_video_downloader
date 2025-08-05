from View.frames.frameAlert import frameAlert
from View.labels.subtitleLabel import subtitleLabel
from View.components.progressBar import progresBar

class progressBarPage:
    def __init__(self):
        self._frameBar = frameAlert()
        self._progress = progresBar(self._frameBar.getRoot())
        subtitleLabel(self._frameBar.getRoot(), "Downloading...", 10 , 20)
        
    def startProcess(self):
        self._progress.startProcess()
        self._frameBar.show()
        
    def stopProgress(self): 
        self._progress.stopProcess()
        self._frameBar.closeWindow()
       
        
        