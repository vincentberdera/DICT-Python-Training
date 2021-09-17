from tkinter import *

expr = " " # global variable
op = ""
x = []
def clear():
    result.set("")
    global expr # first, referencing the global variable
    expr = "" # utilizing the global variable

def process(value):
    global expr # referencing the global variable expr
    expr = expr + str(value)     # expr="8+2"
    result.set(expr)
 ##########################
    global op
    if value=="+":
        op = "+"
    elif value=="-":
        op = "-"
    elif value=="*":
        op = "*"
    elif value=="/":
        op = "/"
  ###########################

def evaluate(): # callback function
    global expr
    r = eval(expr) #    eval(1+6)
    result.set(str(r))
    expr = ""

def myown():
    global expr
    global op
    global x # list variable

    x = expr.split(op) # "8+2"
    left = int(x[0]) # 8
    right = int(x[1]) # 2

    if op == "+":
        r = left+right
    elif op == "-":
        r = left-right
    elif op == "*":
        r = left*right
    elif op == "/":
        if right==0:
            r = "Division by zero error"
        else:
            r = left/right

    result.set(str(r))
    expr = ""

window = Tk()
window.geometry("400x400")
window.resizable(0,0)
window.title("Simple Calculator")

#Text Variable Declaration
result = StringVar()

resE = Entry(window, bd=3, font="Tahoma", textvariable = result, justify = RIGHT, state=DISABLED)
resE.place(x=50,y=30, height=40, width=300)

seven = Button(window, text="7", font="Tahoma", width=7, command=lambda:process(7) )
seven.place(x=50,y=80)

eight = Button(window, text="8", font="Tahoma", width=7, command=lambda: process(8))
eight.place(x=125,y=80)

nine = Button(window, text="9", font="Tahoma", width=7, command=lambda: process(9))
nine.place(x=200,y=80)

four = Button(window, text="4", font="Tahoma", width=7, command=lambda: process(4))
four.place(x=50,y=120)

five = Button(window, text="5", font="Tahoma", width=7, command=lambda: process(5))
five.place(x=125,y=120)

six = Button(window, text="6", font="Tahoma", width=7, command=lambda: process(6))
six.place(x=200,y=120)

one = Button(window, text="1", font="Tahoma", width=7, command=lambda: process(1))
one.place(x=50,y=160)

two = Button(window, text="2", font="Tahoma", width=7, command=lambda: process(2))
two.place(x=125,y=160)

three = Button(window, text="3", font="Tahoma", width=7, command=lambda: process(3))
three.place(x=200,y=160)

zero = Button(window, text="0", font="Tahoma", width=7, command=lambda: process(0))
zero.place(x=50,y=200)

equal = Button(window, text="=", font="Tahoma", width=7, command= evaluate )
equal.place(x=125,y=200)

clear = Button(window, text="Clear", font="Tahoma", width=7, command=clear)
clear.place(x=200,y=200)

div = Button(window, text="/", font="Tahoma", width=7, command=lambda: process("/"))
div.place(x=280,y=80)

mult = Button(window, text="*", font="Tahoma", width=7, command=lambda: process("*"))
mult.place(x=280,y=120)

sub = Button(window, text="-", font="Tahoma", width=7, command=lambda: process("-"))
sub.place(x=280,y=160)

add = Button(window, text="+", font="Tahoma", width=7,command=lambda: process("+"))
add.place(x=280,y=200)

window.mainloop()