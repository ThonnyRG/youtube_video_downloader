from View.buttons.blueButton import blueButton
from View.buttons.clearButton import clearButton
from View.frames.defaultFrame import defaultFrame
from View.labels.titleLabel import titleLabel

def main():
    blankP = defaultFrame("Warning")
    labelTittle = titleLabel(blankP.getRoot(), "Warning",200, 40)
    def a():
        print("Python is trash")
    yesButton = blueButton(blankP.getRoot(), "Yes", a, 75, 400)
    noButton = blueButton(blankP.getRoot(), "No", a, 300, 400)
    noClearButton = clearButton(blankP.getRoot(), "CLEAR", a, 100, 100)
    # linkField = textBox(blankP.getRoot())
    # linkField.setText("Python is trash")
    # linkField.setFont("roboto", 22)
    # linkField.setSize(45,450)
    # linkField.setPosition(30,237)
    # linkField.setColor("#9AA0A6")
 
    # browseButton = button(blankP.getRoot())
    # browseButton.setText("Browse")
    # browseButton.setForeGround("#ffffff")
    # browseButton.setBackgroud("#4285F4")
    # browseButton.setSize(47, 98)
    # browseButton.setBorderless()
    # browseButton.setPlace(384, 170)
       
    # browseButton = mtk.Button(blankP.getRoot(), text = "No", font = "Roboto 20", fg = "#ffffff", bg = "#4285F4",borderless = 1,activebackground="#315b9e")
    # browseButton.pack(padx=15 ,pady= 20)
    # browseButton.place(x = 300, y = 400)
  
    # noButton = mtk.Button(blankP.getRoot(), text = "Yes", font = "Roboto 20", fg = "#ffffff", bg = "#4285F4",borderless = 1,activebackground="#315b9e")
    # noButton.pack(padx=15 ,pady= 20)
    # noButton.place(x = 100, y = 400)
  
    blankP.show()
    
if __name__=="__main__":
    main()
