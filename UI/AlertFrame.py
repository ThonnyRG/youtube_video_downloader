import tkinter as tk
import tkmacosx as mtk

class AlertFrame():

   
    def __init__(Self, AlertName):
        Self.AlertName = AlertName
        
    def setAlert(type):
        Alert = tk.Tk()
        Alert.geometry("500x200")
        Alert.title("Warning")
        Alert.resizable(width = False, height= False)
        Label = tk.Label(Alert, text = type.AlertName, font = ('Roboto', 16))
        Label.place(relx=0.5, y=50, anchor="center")
    
        
        yesButton = mtk.Button(Alert, text = "OK",font = "Roboto 20" , fg = "#FFFFFF", bg = "#D2E3FC")
        yesButton.place(relx=0.5, rely=0.75, anchor= "center") 

        Alert.mainloop()
       