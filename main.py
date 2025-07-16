from View.frameBlank import FrameWhite
from View.src.button import button
from View.src.label import label
from View.src.textBox import textBox
from tkinter import messagebox

def main():
    blankP = FrameWhite()
    labelTittle = label(blankP.getRoot())
    labelTittle.setFont("Roboto 24 bold")
    labelTittle.setText("Youtube Video downloader")
    labelTittle.setBackground("#222222")
    labelTittle.setPosition(100, 40)
    
    linkField = textBox(blankP.getRoot())
    linkField.setText("Python is trash")
    linkField.setFont("roboto", 22)
    linkField.setSize(45,450)
    linkField.setPosition(30,237)
    linkField.setColor("#9AA0A6")
  
    browseButton = button(blankP.getRoot())
    browseButton.setText("Browse")
    browseButton.setFont("Roboto 20")
    browseButton.setForeGround("#ffffff")
    browseButton.setBackgroud("#4285F4")
    browseButton.setSize(47, 98)
    browseButton.setBorderless()
    browseButton.setPlace(384, 170)
    
    def pythonIsTrash():
        print("python is trash")
        
    browseButton.setAction(pythonIsTrash)
    # browseButton = mtk.Button(root, text = "Browse", font = "Roboto 20", fg = "#ffffff", bg = "#4285F4", height= 47,width=98,  borderless = 1,activebackground="#315b9e")
    # browseButton.place(x = 384, y = 170)
   
    blankP.show()
    
if __name__=="__main__":
    main()
