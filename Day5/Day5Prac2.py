from tkinter import *
import math

class coeficients():
    def getA(self):
        return float(coefAE.get())
    def getB(self):
        return float(coefBE.get())
    def getC(self):
        return float(coefCE.get())

class Quadratic(coeficients):

    def evaluate(self, x):
        x = (self.getA()*x*x) + (self.getB() * x) + self.getC()
        return x

    def Discriminant(self):
        discriminant = (self.getB() * self.getB()) - (4 * self.getA() * self.getC())
        return discriminant

    def isImaginaryRoots(self):
        if self.Discriminant() < 0:
            root.set("The roots are imaginary.")
            square.set("")

    def isRealRoots(self):
        if self.Discriminant() >= 0:
            root.set(f"The roots are real: x1 = {self.firstRoot()} ; x2 = {self.secondRoot()}")
            self.isPerfectSquare()

    def firstRoot(self):
        root1 = (-self.getB() + math.sqrt(self.Discriminant())) / (2 * self.getA())
        return root1

    def secondRoot(self):
        root2 = (-self.getB() - math.sqrt(self.Discriminant())) / (2 * self.getA())
        return root2

    def isPerfectSquare(self):
        if self.firstRoot() == self.secondRoot():
            square.set("It is a perfect square.")
        else:
            square.set("It is not a perfect square.")

MyClass = Quadratic()


def calculate():
    try:
        quadraticExpression.set("")
        root.set("")
        result.set("")
        square.set("")

        x = float(eXE.get())

        quadraticExpression.set(f"Quadratic Expression:{coefAE.get()}x2+{coefBE.get()}x+{coefCE.get()}=0")
        MyClass.isRealRoots()
        MyClass.isImaginaryRoots()
        result.set(f"Result: {MyClass.evaluate(x)}")

    except ValueError as e:
        quadraticExpression.set("Error due to: Can't accept non integer\nvalue/There is an empty space")


def clear():
    coeficientA.set("")
    coeficientB.set("")
    coeficientC.set("")
    quadraticExpression.set("")
    root.set("")
    square.set("")
    x.set("")
    result.set("")


window = Tk() #instantiation of tkinter
window.geometry("600x500")
window.resizable(0,0)
window.title("BMI Calculator")

#Text Variables Declaration
quadraticExpression = StringVar()
coeficientA = StringVar()
coeficientB = StringVar()
coeficientC = StringVar()
root = StringVar()
square = StringVar()
x = StringVar()
result = StringVar()


titleL = Label(window, text="Quadratic Equation", font="Tahoma")
titleL.place(x=200,y=30)

coefAL = Label(window,text="Enter coefficient: ", font="Tahoma")
coefAL.place(x=130, y=100)

coefAE = Entry(window, bd=3, textvariable = coeficientA)
coefAE.place(x=300,y=100)

coefBL = Label(window,text="Enter coefficient: ", font="Tahoma")
coefBL.place(x=130, y=130)

coefBE = Entry(window, bd=3, textvariable = coeficientB)
coefBE.place(x=300,y=130)

coefCL = Label(window,text="Enter coefficient: ", font="Tahoma")
coefCL.place(x=130, y=160)

coefCE = Entry(window, bd=3, textvariable = coeficientC)
coefCE.place(x=300,y=160)

quadE = Label(window, bd=3, textvariable=quadraticExpression, font="Tahoma")
quadE.place(x=130, y=210)

rootLE = Label(window, textvariable=root, font="Tahoma")
rootLE.place(x=130, y=240)

squareLE = Label(window, textvariable=square, font="Tahoma")
squareLE.place(x=130, y=270)

eXL = Label(window, text="Evaluating the expression: ", font="Tahoma")
eXL.place(x=130, y=320)

eXL = Label(window, text="Enter x: ", font="Tahoma")
eXL.place(x=130, y=350)

eXE = Entry(window, bd=3, textvariable = x)
eXE.place(x=300,y=350)

resultLE = Label(window, textvariable=result, font="Tahoma")
resultLE.place(x=130, y=380)

calc = Button(window, text="Calculate", width=8, command = calculate )
calc.place(x=290, y=430)

clear = Button(window, text="Clear", width=8, command = clear )
clear.place(x=370, y=430)

window.mainloop()