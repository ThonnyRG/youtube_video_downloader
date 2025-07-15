from View.frameBlank import FrameWhite
from View.src.label import label
from View.src.textBox import textBox

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
    
    blankP.show()
    
if __name__=="__main__":
    main()
