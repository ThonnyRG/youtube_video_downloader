
from View.buttons.blueButton import blueButton
from View.frames.frameAlert import frameAlert
from View.labels.subtitleLabel import subtitleLabel
from View.labels.titleLabel import titleLabel


class alertPage():
    def __init__(self, message: str):
        self._frameAlert = frameAlert()
        self._message = message
        self._setupPage()
        pass
    
    def _setupPage(self):
        titleLabel(self._frameAlert.getRoot(), "Attention", 5, 5)
        subtitleLabel(self._frameAlert.getRoot(), self._message,10 ,5).setWrap(400)
        blueButton(self._frameAlert.getRoot(), "ok", self._frameAlert.closeWindow, 190, 135)
        self._frameAlert.show()