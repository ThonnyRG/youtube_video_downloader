from Controller.userActions import userActions

from Model.fileDownloader import fileDownloader
from Model.mediaDownloader import mediaDownloader
from View.buttons.blueButton import blueButton
from View.fieldText.defaultTextbox import defaultTextBox
from View.frames.defaultFrame import defaultFrame
from View.labels.subtitleLabel import subtitleLabel
from View.labels.titleLabel import titleLabel
from View.labels.underlineLabel import underlineLabel
from View.pages.alertPage import alertPage

class mainPage():
    def __init__(self):
        self.isDownloading = False
        self._setupWindow()
                         
    def _setupWindow(self):
        frmMain = defaultFrame("PyMedia downloader")
        titlePage = titleLabel(frmMain.getRoot(), "PyMedia downloader", 100, 30)
        instructionLabel = subtitleLabel(frmMain.getRoot(), "Enter in the box the full URL of your video.", 10, 1)
        instructionLabel.setWrap(401)
        saveToLabel = subtitleLabel(frmMain.getRoot(), "Save to:", 10, 10)
        saveToLabel.setWrap(77)

        saveFolder = fileDownloader()
        
        def changeFolderAndUpdate():
            newFolder = saveFolder.selectFolder()
            
            fileRevealLabel.updateText(newFolder)
             
        fileRevealLabel = underlineLabel(frmMain.getRoot(), saveFolder.getCurrentFolder(), 10, 10, changeFolderAndUpdate, True)

        linkUrl = defaultTextBox(frmMain.getRoot(),"ENTER URL VIDEO", 10, 20)         

        def downloadAction():
            if self.isDownloading:
                return
            
            currentURL = linkUrl.getText()
            currentFolder = saveFolder.getCurrentFolder()
            if not currentURL or currentURL.strip() == "ENTER URL VIDEO" or currentURL.strip() == "":
                alertPage("Error: Please enter a valid URL")
                return
            downloader = mediaDownloader(currentURL.strip(), currentFolder) 
            result = downloader.downloadMedia()
            alertPage(result)
            
        pasteButton = blueButton(frmMain.getRoot(), "Paste", lambda: [linkUrl.clearText, userActions().pasteFromClipBoard(frmMain, linkUrl)], 175, 325)
        clearButton = blueButton(frmMain.getRoot(), "Clear", linkUrl.clearText, 25, 325)       
        downloadButton = blueButton(frmMain.getRoot(), "Download", downloadAction, 325, 325)
        frmMain.show()    
        