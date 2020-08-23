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
          font = self.headerFont).grid(row=3,column =1)
    Label(self,text = "25%",font = self.headerFont).grid(row=0,column=3)

    Label(self, text = "Lab Asessment 1").grid(row = 4, column = 0)
    self.txtLab1 = Entry(self)
    self.txtLab1.grid(row = 4, column = 1)
    self.txtLab1.insert(0, "")
    Label(self,text = "10%").grid(row=4,column=2)

    Label(self, text = "Lab tutorial ").grid(row = 5, column = 0)
    self.txtLab2 = Entry(self)
    self.txtLab2.grid(row = 5, column = 1)
    self.txtLab2.insert(0, "")
    Label(self,text = "5%").grid(row=5,column=2)

    Label(self, text = "Lab tutorial 3,4,5,6 ").grid(row = 6, column = 0)
    self.txtLab3 = Entry(self)
    self.txtLab3.grid(row = 6, column = 1)
    self.txtLab3.insert(0, "")
    Label(self,text = "10%").grid(row=6,column=2)

def addLabTest(self):
    Label(self, text = "Lab Test",
          font = self.headerFont).grid(row=7,column =0)
    Label(self,text = "20%",font = self.headerFont).grid(row=0,column=3)
    
    Label(self, text = "Lab Assignment").grid(row = 8, column = 0)
    self.txtLabTest1 = Entry(self)
    self.txtLabTest1.grid(row = 8, column = 1)
    self.txtLabTest1.insert(0, "")
    Label(self,text = "10%").grid(row=8,column=2)

    Label(self, text = "Code Review").grid(row = 9, column = 0)
    self.txtTest2 = Entry(self)
    self.txtTest2.grid(row = 9, column = 1)
    self.txtTest2.insert(0, "")
    Label(self,text = "10%").grid(row=9,column=2)

def addMiniProject(self):
    Label(self, text = "Mini Project",
          font = self.headerFont).grid(row=10,column =0)
    Label(self,text = "20%",font = self.headerFont).grid(row=0,column=3)

    Label(self, text = "Report").grid(row = 11, column = 0)
    self.txtReport = Entry(self)
    self.txtReport.grid(row = 11, column = 1)
    self.txtReport.insert(0, "")
    Label(self,text = "10%").grid(row=11,column=2)
    
    Label(self, text = "Product & Presentation").grid(row = 12, column = 0)
    self.txtProduct_Presentation = Entry(self)
    self.txtProduct_Presentationt.grid(row = 12, column = 1)
    self.txtProduct_Presentation.insert(0, "")
    Label(self,text = "10%").grid(row=12,column=2)
    
