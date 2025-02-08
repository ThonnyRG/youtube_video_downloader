import tkinter as tk

class AlertFrame():

    
    def __init__(Self, AlertName):
        Self.AlertName = AlertName
        

        
    def setAlert(type):
        Alert = tk.Tk()
        Alert.geometry("200x200")
        Alert.title("Warning")
        Label = tk.Label(Alert, text = type.AlertName, font = ('Roboto', 16))
       