from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.headerFont = ("Helvetica", "16", "bold")
        self.downFont = ("Helvetica", "60", "bold")
        self.title("Coursework Mark Calculate")
        
        self.addQuizzes()
        self.addLabAssessment()
        self.addLabTest()
        self.addMiniProject()
        self.FinalAssessment()
        self.addOutput()
        
        self.geometry("500x550")
    
    

    def addQuizzes(self):
        Label(self, text = "Quizzes",font = self.headerFont).grid(row=1,column =1)
        Label(self,text = "10%",font = self.headerFont).grid(row=1,column=3)
    
        Label(self, text = "Quiz 1").grid(row = 2, column = 0)
        self.txtQuiz1 = Entry(self)
        self.txtQuiz1.grid(row = 2, column = 1)
        self.txtQuiz1.insert(0, "")
        Label(self,text = "4%").grid(row=2,column=2)

        Label(self, text = "Quiz 2,3,4").grid(row = 3, column = 0)
        self.txtQuiz2 = Entry(self)
        self.txtQuiz2.grid(row = 3, column = 1)
        self.txtQuiz2.insert(0, "")
        Label(self,text = "5%").grid(row=3,column=2)

    def addLabAssessment(self):
        Label(self, text = "Lab Assessment",font = self.headerFont).grid(row=4,column =1)
        Label(self,text = "25%",font = self.headerFont).grid(row=4,column=3)

        Label(self, text = "Lab Asessment 1").grid(row = 5, column = 0)
        self.txtLab1 = Entry(self)
        self.txtLab1.grid(row = 5, column = 1)
        self.txtLab1.insert(0, "")
        Label(self,text = "10%").grid(row=5,column=2)

        Label(self, text = "Lab tutorial ").grid(row = 6, column = 0)
        self.txtLab2 = Entry(self)
        self.txtLab2.grid(row = 6, column = 1)
        self.txtLab2.insert(0, "")
        Label(self,text = "5%").grid(row=6,column=2)

        Label(self, text = "Lab tutorial 3,4,5,6 ").grid(row = 7, column = 0)
        self.txtLab3 = Entry(self)
        self.txtLab3.grid(row = 7, column = 1)
        self.txtLab3.insert(0, "")
        Label(self,text = "10%").grid(row=7,column=2)

    def addLabTest(self):
        Label(self, text = "Lab Test",font = self.headerFont).grid(row=8,column =1)
        Label(self,text = "20%",font = self.headerFont).grid(row=8,column=3)
    
        Label(self, text = "Lab Assignment").grid(row = 9, column = 0)
        self.txtLabTest1 = Entry(self)
        self.txtLabTest1.grid(row = 9, column = 1)
        self.txtLabTest1.insert(0, "")
        Label(self,text = "10%").grid(row=9,column=2)

        Label(self, text = "Code Review").grid(row = 10, column = 0)
        self.txtLabTest2 = Entry(self)
        self.txtLabTest2.grid(row = 10, column = 1)
        self.txtLabTest2.insert(0, "")
        Label(self,text = "10%").grid(row=10,column=2)

    def addMiniProject(self):
        Label(self, text = "Mini Project",font = self.headerFont).grid(row=11,column =1)
        Label(self,text = "25%",font = self.headerFont).grid(row=11,column=3)

        Label(self, text = "Report").grid(row = 12, column = 0)
        self.txtReport = Entry(self)
        self.txtReport.grid(row = 12, column = 1)
        self.txtReport.insert(0, "")
        Label(self,text = "10%").grid(row=12,column=2)
    
        Label(self, text = "Product & Presentation").grid(row = 13, column = 0)
        self.txtProduct = Entry(self)
        self.txtProduct.grid(row = 13, column = 1)
        self.txtProduct.insert(0, "")
        Label(self,text = "15%").grid(row=13,column=2)
    
    def FinalAssessment(self):
        Label(self, text = "Final Assessment",font = self.headerFont).grid(row = 14, column = 1)
        Label(self,text = "20%",font = self.headerFont).grid(row=14,column=3)
    
        Label(self, text = "Final Assessment").grid(row = 15, column = 0)
        self.txtFinal = Entry(self)
        self.txtFinal.grid(row = 15, column = 1)
        self.txtFinal.insert(0, "")
        Label(self,text = "20%").grid(row=15,column=2)

    def addOutput(self):
        self.btnCalc = Button(self, text = "calculate grade and get data")
        self.btnCalc.grid(row = 16, column = 1)
        self.btnCalc["command"] = self.calculate
        
        Label(self, text = "Overall Percent").grid(row = 20, column = 0)
        self.lblTotal = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        self.lblTotal.grid(row = 20, column = 1, sticky = "we")

        Label(self, text = "Need To Pass").grid(row = 21, column = 0)
        self.lblNeed = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        self.lblNeed.grid(row = 21, column = 1, sticky = "we")
 
    def calculate(self):
        Quiz1 = int(self.txtQuiz1.get())
        Quiz2 = int(self.txtQuiz2.get())
       

        QuizTot = Quiz1 + Quiz2 
    
        Lab1 = int(self.txtLab1.get())
        Lab2 = int(self.txtLab2.get())
        Lab3 = int(self.txtLab3.get())
    
        LabAssessmentTot= Lab1 + Lab2 + Lab3

        LabTest1 = int(self.txtLabTest1.get())
        LabTest2 = int(self.txtLabTest2.get())

        LabTestTot = LabTest1 + LabTest2

        Report = int(self.txtReport.get())
        Product = int(self.txtProduct.get())

        MiniProjectTot=Report+Product

        Finals = int(self.txtFinal.get()) 

        total = (QuizTot) + (LabAssessmentTot) + (LabTestTot)+(MiniProjectTot)+(Finals)
        self.lblTotal["text"] = "%.2f" % total
    
        NeedPass=100-total
        self.lblNeed["text"] = "%.2f" % NeedPass 
        
        if total >= 99.00:
            Label(self, text = "A",font=self.downFont,bg="black",fg="green").grid(row = 22, column = 1)
        elif total >= 70.00: 
            Label(self, text = "B",font=self.downFont,bg="black",fg="yellow").grid(row = 22, column = 1)
        elif total >= 50.00:
            Label(self, text = "C",font=self.downFont,bg="black",fg="yellow").grid(row = 22, column = 1)
        else : 
            Label(self, text = "FAIL",font=self.downFont,bg="black",fg="red").grid(row = 22, column = 1)      
    
        
        
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()