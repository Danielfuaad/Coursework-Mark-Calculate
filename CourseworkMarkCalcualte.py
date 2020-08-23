from tkinter import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)

    self.headerFont = ("Helvetica", "16", "bold italic")
    
    self.title("Coursework Mark Calculate")
    self.addQuizzes()
    self.addLabs()
    self.addExams()
    self.addProj()
    self.addOutput()
    self.geometry("500x350")