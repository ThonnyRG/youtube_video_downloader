import tkinter as tk

class AlertFrame():

    
    def __init__(Self, AlertName):
        Self.AlertName = AlertName
        
    def setAlert(type):
        Alert = tk.Tk()
        Alert.geometry("500x200")
        Alert.title("Warning")
        Alert.resizable(width = False, height= False)
        Label = tk.Label(Alert, text = type.AlertName, font = ('Roboto', 16))
        Label.place(x=10,y=20)
        
        Alert.mainloop()
       