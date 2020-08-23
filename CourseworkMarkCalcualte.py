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

def addQuizzes(self):
    Label(self, text = "Quizzes",
          font = self.headerFont).grid(row=0,column =1)
    Label(self,text = "10%",font = self.headerFont).grid(row=0,column=3)
    
    Label(self, text = "Quiz 1").grid(row = 1, column = 0)
    self.txtQuiz1 = Entry(self)
    self.txtQuiz1.grid(row = 1, column = 1)
    self.txtQuiz1.insert(0, "")
    Label(self,text = "4%").grid(row=1,column=2)

    Label(self, text = "Quiz 2,3,4").grid(row = 2, column = 0)
    self.txtQuiz2 = Entry(self)
    self.txtQuiz2.grid(row = 2, column = 1)
    self.txtQuiz2.insert(0, "")
    Label(self,text = "5%").grid(row=2,column=2)

def addLabAssessment(self):
  Label(self, text = "Lab Assessment",
          font = self.headerFont).grid(row=0,column =1)
    Label(self,text = "10%",font = self.headerFont).grid(row=0,column=3)

    Label(self, text = "Lab Asessment 1").grid(row = 1, column = 0)
    self.txtLab1 = Entry(self)
    self.txtLab1.grid(row = 1, column = 1)
    self.txtLab1.insert(0, "")
    Label(self,text = "4%").grid(row=1,column=2)