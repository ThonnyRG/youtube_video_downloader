from View.frameBlank import FrameWhite
from View.src.label import label

def main():
    blankP = FrameWhite()
    labelTittle = label(blankP.getRoot())
    labelTittle.setFont("Roboto 24 bold")
    labelTittle.setText("PYTHON IS TRASH")
    labelTittle.setBackground("#222222")
    labelTittle.setPosition(100, 40)
    blankP.show()
    
if __name__=="__main__":
    main()
