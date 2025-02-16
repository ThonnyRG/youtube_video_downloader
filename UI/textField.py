from tkinter import ttk


class textField():
    def __init__(self, width, height,placeX, placeY,message):
        self.width = width
        self.height = height
        self.placeX = placeX
        self.placeY = placeY
        self.message = message
        
    def buildTextbox(self):
        textBox = ttk.Entry(width= self.width, justify = ttk.left)
        textBox.place(self.placeX, self.placeY)
        textBox.insert(self.message)

        