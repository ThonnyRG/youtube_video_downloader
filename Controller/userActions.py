from View.components.frame import frame
from View.fieldText.defaultTextbox import defaultTextBox


class userActions:
    def pasteFromClipBoard(self, rootFrame : frame, rootTextbox: defaultTextBox):
        try:
            clipboardContent = rootFrame.getRoot().clipboard_get()
            rootTextbox.insertText(clipboardContent)
        except Exception as e:
            rootTextbox.clearText()
            
        return self