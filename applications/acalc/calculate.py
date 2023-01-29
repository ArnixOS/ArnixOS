from tkinter import END
from tkinter.messagebox import showerror
from math import *

def calculate(opearation: str , self: str):
    try:
        output = eval(opearation)
    except Exception:
        showerror("Error" , "An exception occured preventing this operation")

    self.config(state="normal")
    
    try:
        self.insert(END , f"Output of {opearation}= {output}\n")
    except UnboundLocalError:
        pass

    self.config(state="disabled")
